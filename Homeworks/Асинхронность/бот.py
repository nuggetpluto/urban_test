from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


TOKEN = '7222268649:AAH48XPDF8yYUqbPvg5rDYBtrW8ci1tvqHw'

# Инициализация бота и диспетчера с хранением состояний в памяти
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Определение группы состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создание клавиатуры с кнопками "Рассчитать" и "Информация"
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard.add(button_calculate, button_info)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Выберите действие:', reply_markup=keyboard)

# Функция для ввода возраста, реагирующая на нажатие кнопки "Рассчитать"
@dp.message_handler(text='Рассчитать')
async def set_age(message: Message):
    await message.answer('Введите свой возраст:')
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

    # Пример расчета по формуле Миффлина - Сан Жеора для мужчин
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
