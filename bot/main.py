import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import time
import logging

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

# loading local environment variables
load_dotenv()

TELEGRAM_API_KEY = os.getenv("BOT_API_KEY")
bot = Bot(token=TELEGRAM_API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    current_user = message.from_user
    await message.answer(f"Hello there, <b><i>{current_user['first_name']}!</i></b>", parse_mode="HTML")
    time.sleep(1)
    await message.answer("This is <b>Salary</b> bot 🤖", parse_mode="HTML")
    time.sleep(1)
    await message.answer(
        "I can help you with calculating your monthly salary",
        parse_mode="HTML",
    )
    time.sleep(1)


if __name__ == "__main__":
    executor.start_polling(dp)