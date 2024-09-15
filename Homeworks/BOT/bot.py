from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from crudfunctions import initiate_db, get_all_products, add_user, is_included

TOKEN = '****************************************************************'

# Инициализация бота и диспетчера с хранением состояний в памяти
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Инициализация базы данных
initiate_db()

# Обычная клавиатура с кнопками "Рассчитать", "Информация", "Купить" и "Регистрация"
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = types.KeyboardButton('Рассчитать')
button_info = types.KeyboardButton('Информация')
button_buy = types.KeyboardButton('Купить')
button_register = types.KeyboardButton('Регистрация')
keyboard.add(button_calculate, button_info, button_buy, button_register)

# Определение классов состояний для регистрации пользователей
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Выберите действие:", reply_markup=keyboard)

# Хэндлер для начала регистрации
@dp.message_handler(text='Регистрация')
async def sing_up(message: Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

# Хэндлер для ввода имени пользователя
@dp.message_handler(state=RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    username = message.text

    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

# Хэндлер для ввода email
@dp.message_handler(state=RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

# Хэндлер для ввода возраста
@dp.message_handler(state=RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    age = message.text

    # Получаем данные из состояний
    data = await state.get_data()
    username = data['username']
    email = data['email']

    # Добавляем пользователя в базу данных
    add_user(username, email, int(age))

    await message.answer(f"Регистрация завершена! Пользователь {username} добавлен.")
    await state.finish()

# Хэндлеры для других команд (например, "Рассчитать", "Информация", "Купить")

@dp.message_handler(text='Рассчитать')
async def calculate_handler(message: types.Message):
    await message.answer("Функция расчета пока не реализована.")

@dp.message_handler(text='Информация')
async def info_handler(message: types.Message):
    await message.answer("Это бот для покупки товаров!")

@dp.message_handler(text='Купить')
async def buy_handler(message: types.Message):
    products = get_all_products()
    if products:
        for product in products:
            product_id, product_name, description, price, photo_path = product
            caption = f"Название: {product_name}\nОписание: {description}\nЦена: {price} руб."

            # Отправляем фото товара вместе с описанием
            try:
                with open(photo_path, 'rb') as photo:
                    await message.answer_photo(photo=photo, caption=caption)
            except FileNotFoundError:
                await message.answer(f"Фото для {product_name} не найдено!\n{caption}")
    else:
        await message.answer("Список продуктов пуст.")


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
