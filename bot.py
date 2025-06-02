from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from config import TOKEN
from handlers import questions
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
questions.register(dp)
if __name__ == '__main__': executor.start_polling(dp)