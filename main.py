from os import getenv
import asyncio

from aiogram import Dispatcher, Bot, html
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
