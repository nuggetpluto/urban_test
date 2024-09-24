from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import asyncio

api = '7007259145:AAEOyvlboPt47U3JpjSCO6Omm4N64ik0FjM'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

def create_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    buttons = [
        types.KeyboardButton("Рассчитать"),
        types.KeyboardButton("Информация"),
        types.KeyboardButton("Купить")
    ]
    kb.add(*buttons)
    return kb

def create_inline_keyboard():
    kb = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories'),
        InlineKeyboardButton("Формулы расчёта", callback_data='formulas'),
        InlineKeyboardButton("Product1", callback_data='product_buying'),
        InlineKeyboardButton("Product2", callback_data='product_buying'),
        InlineKeyboardButton("Product3", callback_data='product_buying'),
        InlineKeyboardButton("Product4", callback_data='product_buying')
    ]
    kb.add(*buttons)
    return kb

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. Нажми "Рассчитать", чтобы начать.',
                         reply_markup=create_keyboard())

@dp.message_handler(lambda message: message.text == "Рассчитать")
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=create_inline_keyboard())

@dp.message_handler(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):
    products = [
        {"name": "Product1", "description": "Описание 1", "price": 100,
         "image":"photos/photo1.jpg"},
        {"name": "Product2", "description": "Описание 2", "price": 200,
         "image":"photos/photo2.jpg"},
        {"name": "Product3", "description": "Описание 3", "price": 300,
         "image": "photos/photo3.jpg"},
        {"name": "Product4", "description": "Описание 4", "price": 400,
         "image": "photos/photo4.jpg"}
    ]

    for product in products:
        await message.answer(f'Название: {product["name"]} | Описание: '
                             f'{product["description"]} | Цена: {product["price"]} руб.')
        with open(product["image"], 'rb') as photo:  # Открываем файл фотографии
            await message.answer_photo(photo=photo)

    await message.answer('Выберите продукт для покупки:', reply_markup=create_inline_keyboard())

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора:\n"
                              "Для мужчин: BMR = 10 * вес + 6.25 * рост - 5 * возраст + 5\n"
                              "Для женщин: BMR = 10 * вес + 6.25 * рост - 5 * возраст - 161")
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма калорий: {calories} ккал в день.')
    await state.finish()

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)