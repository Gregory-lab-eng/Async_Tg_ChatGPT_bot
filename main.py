from os import getenv
import asyncio
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot, html, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from openai import OpenAI


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
OPENAI_API_KEY = getenv("OPENAI_API_KEY")

dp = Dispatcher()
client = OpenAI()



@dp.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Gre loves, {html.bold(message.from_user.full_name)}!")


@dp.message(Command('random'))
async def command_random_handler(message: Message) -> None:
    response = client.responses.create(
        model="gpt-4o-mini-2024-07-18",
        input=str(message),
        instructions="дай любой рандомный факт"
    )
    await message.answer(f"{response.output_text}")


@dp.message(F.text)
async def text_handler(message: Message) -> None:
    response = client.responses.create(
        model="gpt-4o-mini-2024-07-18",
        input=str(message),
        instructions="Разговаривай как молодой влюбленные поэт"
    )
    await message.answer(f"{response.output_text}")

#f"Gre still loves you, {html.bold(message.from_user.full_name)}!
async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())