import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TELEGRAM_TOKEN, API_URL

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_message(message: types.Message):
    user_question = message.text
    try:
        response = requests.get(API_URL, params={"question": user_question})
        answer = response.json().get("answer", "Не удалось получить ответ.")
    except Exception as e:
        answer = f"Ошибка: {e}"
    await message.reply(answer)

if name == "__main__":
    executor.start_polling(dp, skip_updates=True)