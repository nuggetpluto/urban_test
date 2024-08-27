from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import Message

TOKEN = '******************************** '
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')

# Обработка всех остальных сообщений
@dp.message_handler()
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
