import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import time
import logging
from salary import calculate_salary

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
        "I can help you with calculating your <b>monthly salary</b>",
        parse_mode="HTML",
    )
    time.sleep(1)
    await message.answer("To calculate your salary I need following data:", parse_mode="HTML")
    time.sleep(1)
    await message.answer("1) Total hours you worked this month \n"
                         "2) Total Business hours you worked\n"
                         "3) Total hours you worked Beyond Business Hours\n"
                         "4) Working days\n"
                         "5) Your Fixed salary", parse_mode="HTML")
    time.sleep(1)
    await message.answer("Please, provide it in such format", parse_mode="HTML")
    await message.answer(
        "<i>total_hours<b>|</b>business_hours<b>|</b>beyond_b_hours<b>|</b>working_days<b>|</b>fixed_salary</i>\n\n"
        "For example:\n"
        "195.98|183.98|11.99|23|500", parse_mode="HTML")


@dp.message_handler(content_types=["text"])
async def salary_calculation(message: types.Message):
    if "|" in message.text:
        query: list = [param.strip() for param in message.text.split("|")]

        try:
            total_hours = float(query[0])
            business_hours = float(query[1])
            beyond_b_hour = float(query[2])
            working_days = int(query[3])
            fixed_salary = int(query[4])

            result = calculate_salary(total_hours, business_hours, beyond_b_hour, working_days, fixed_salary)

            salary = "{:.2f}".format(result['salary'])
            b_hours_bonuses = "{:.2f}".format(result['business'])
            beyond_b_hours_bonuses = "{:.2f}".format(result['beyond'])

            await message.answer("Processing...")
            time.sleep(1)
            await message.answer(f"Salary: <b>${salary}</b>\n\n"
                                 f"Business hours bonuses: <b>${b_hours_bonuses}</b>\n"
                                 f"Beyond business hours bonuses: <b>${beyond_b_hours_bonuses}</b>", parse_mode="html")

        except IndexError:
            await message.answer("❗ Invalid query format. Try again")

        except ValueError:
            await message.answer("❗ Invalid query format. Try again")
    else:
        await message.answer("❗ Invalid query format. Try again")


if __name__ == "__main__":
    while True:
        try:
            executor.start_polling(dp, skip_updates=True)
        except:
            pass
