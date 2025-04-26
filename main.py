from os import getenv
import asyncio
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot, html, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


@dp.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Gre loves, {html.bold(message.from_user.full_name)}!")


@dp.message(F.text)
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Gre still loves you, {html.bold(message.from_user.full_name)}!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())