from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# Токен вашего бота
TOKEN = '********************************'

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
keyboard.add(button_calculate, button_info)

# Inline-клавиатура с кнопками "Рассчитать норму калорий" и "Формулы расчёта"
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_calories = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
inline_formulas = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
inline_keyboard.add(inline_calories, inline_formulas)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Выберите действие:', reply_markup=keyboard)

# Функция для вывода Inline-клавиатуры
@dp.message_handler(text='Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

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
