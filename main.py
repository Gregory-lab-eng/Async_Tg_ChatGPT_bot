from os import getenv
import asyncio
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import main_router

load_dotenv()
TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass