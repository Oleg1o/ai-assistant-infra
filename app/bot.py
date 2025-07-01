from aiogram import Bot, Dispatcher, types
from config import TELEGRAM_TOKEN, API_URL
import aiohttp
import asyncio

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_message(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json={"question": message.text}) as resp:
            data = await resp.json()
            answer = data.get("answer", "Ошибка обработки.")

    await message.reply(answer)

if name == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)