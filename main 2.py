
import logging
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Бот работает!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
