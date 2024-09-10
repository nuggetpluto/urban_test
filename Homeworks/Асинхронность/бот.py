from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from crud_functions import initiate_db, get_all_products, add_product

TOKEN = '********************************'

# Инициализация бота и диспетчера с хранением состояний в памяти
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Инициализация базы данных
initiate_db()


# Обычная клавиатура с кнопками "Рассчитать", "Информация" и "Купить"
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = types.KeyboardButton('Рассчитать')
button_info = types.KeyboardButton('Информация')
button_buy = types.KeyboardButton('Купить')  # Кнопка "Купить"
keyboard.add(button_calculate, button_info, button_buy)

# Inline-клавиатура для продуктов
buy_menu = InlineKeyboardMarkup(row_width=2)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}! Я бот, помогающий твоему здоровью. Выберите действие:', reply_markup=keyboard)

# Обновляем функцию get_buying_list для вывода продуктов из базы данных
async def get_buying_list(message: Message):
    products = get_all_products()  # Получаем список продуктов из базы данных

    if products:
        for product in products:
            product_id, product_name, description, price, photo_path = product
            caption = f"Название: {product_name} | Описание: {description} | Цена: {price} руб."

            # Добавляем кнопку "Купить" для каждого продукта
            buy_button = InlineKeyboardButton(text=f"Купить {product_name}", callback_data=f"buy_{product_id}")
            buy_menu.add(buy_button)

            # Отправляем сообщение с продуктом и его фото
            await message.answer_photo(photo=open(photo_path, 'rb'), caption=caption)

        # Отправляем Inline меню
        await message.answer("Выберите продукт для покупки:", reply_markup=buy_menu)
    else:
        await message.answer("Список продуктов пуст.")

# Message хэндлер на текст "Купить", вызывает функцию get_buying_list
@dp.message_handler(text='Купить')
async def handle_buy_message(message: Message):
    await get_buying_list(message)

# Callback хэндлер для обработки покупки
@dp.callback_query_handler(lambda call: call.data.startswith('buy_'))
async def send_confirm_message(call: CallbackQuery):
    product_id = int(call.data.split('_')[1])  # Получаем ID продукта
    products = get_all_products()

    # Ищем продукт по ID
    for product in products:
        if product[0] == product_id:
            product_name = product[1]
            await call.message.answer(f"Вы успешно приобрели {product_name}!")
            break

    await call.answer()

# Обработка всех остальных сообщений
@dp.message_handler()
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
