from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

TOKEN = '**********************************************************************'

# Инициализация бота и диспетчера с хранением состояний в памяти
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Определение группы состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Обычная клавиатура с кнопками "Рассчитать" и "Информация"
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = types.KeyboardButton('Рассчитать')
button_info = types.KeyboardButton('Информация')
button_buy = types.KeyboardButton('Купить')  # Добавляем кнопку "Купить"
keyboard.add(button_calculate, button_info, button_buy)

# Inline-клавиатура с продуктами
buy_menu = InlineKeyboardMarkup(row_width=2)
inline_product1 = InlineKeyboardButton(text="Product1", callback_data="product1")
inline_product2 = InlineKeyboardButton(text="Product2", callback_data="product2")
inline_product3 = InlineKeyboardButton(text="Product3", callback_data="product3")
inline_product4 = InlineKeyboardButton(text="Product4", callback_data="product4")
buy_menu.add(inline_product1, inline_product2, inline_product3, inline_product4)

# Inline-клавиатура для расчета калорий
calories_menu = InlineKeyboardMarkup(row_width=1)
inline_calories = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
inline_formulas = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
calories_menu.add(inline_calories, inline_formulas)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}! Я бот, помогающий твоему здоровью. Выберите действие:', reply_markup=keyboard)

# Функция для вывода Inline-клавиатуры с продуктами
@dp.message_handler(text='Купить')
@dp.message_handler(text='Купить')
async def get_buying_list(message: Message):
    # Отправляем информацию о каждом товаре с фотографиями
    products_info = [
        ("Product1", "Описание 1", 100, 'photos/photo1.jpg'),
        ("Product2", "Описание 2", 200, 'photos/photo2.jpg'),
        ("Product3", "Описание 3", 300, 'photos/photo3.jpg'),
        ("Product4", "Описание 4", 400, 'photos/photo4.jpg')
    ]

    for product_name, description, price, photo_path in products_info:
        caption = f"{product_name} - {description}\nЦена: {price} руб."
        await message.answer_photo(photo=open(photo_path, 'rb'), caption=caption)

    # Отправляем кнопки для выбора товара
    await message.answer('Выберите продукт для покупки:', reply_markup=buy_menu)


# Функция для вывода Inline-клавиатуры с калькулятором калорий
@dp.message_handler(text='Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию для расчета калорий:', reply_markup=calories_menu)

# Обработчики для каждого продукта
@dp.callback_query_handler(text='product1')
async def buy_product1(call: CallbackQuery):
    await call.message.answer_photo(photo=open('photos/photo1.jpg', 'rb'))
    await call.message.answer("Вы успешно приобрели Product1!")
    await call.answer()

@dp.callback_query_handler(text='product2')
async def buy_product2(call: CallbackQuery):
    await call.message.answer_photo(photo=open('photos/photo2.jpg', 'rb'))
    await call.message.answer("Вы успешно приобрели Product2!")
    await call.answer()

@dp.callback_query_handler(text='product3')
async def buy_product3(call: CallbackQuery):
    await call.message.answer_photo(photo=open('photos/photo3.jpg', 'rb'))
    await call.message.answer("Вы успешно приобрели Product3!")
    await call.answer()

@dp.callback_query_handler(text='product4')
async def buy_product4(call: CallbackQuery):
    await call.message.answer_photo(photo=open('photos/photo4.jpg', 'rb'))
    await call.message.answer("Вы успешно приобрели Product4!")
    await call.answer()

# Обработка нажатия на кнопку "Формулы расчёта"
@dp.callback_query_handler(text='formulas')
async def get_formulas(call: CallbackQuery):
    formula = ("Формула Миффлина-Сан Жеора для мужчин: BMR = 10 * вес + 6.25 * рост - 5 * возраст + 5\n"
               "Формула Миффлина-Сан Жеора для женщин: BMR = 10 * вес + 6.25 * рост - 5 * возраст - 161")
    await call.message.answer(formula)

# Функция для ввода возраста (начало машины состояний), при нажатии на "Рассчитать норму калорий"
@dp.callback_query_handler(text='calories')
async def set_age(call: CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

# Функция для ввода роста после возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

# Функция для ввода веса после роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

# Финальная функция для подсчета калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    # Пример расчета по формуле Миффлина-Сан Жеора для мужчин
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5  # BMR для мужчин

    await message.answer(f'Ваша норма калорий: {bmr} ккал/день.')
    await state.finish()

# Обработка всех остальных сообщений
@dp.message_handler()
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
