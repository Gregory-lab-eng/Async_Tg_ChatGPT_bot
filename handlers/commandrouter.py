from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from classes import gpt_client


command_router = Router()

@command_router.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Gre loves, {message.from_user.full_name}!")

@command_router.message(Command('random'))
async def command_random_handler(message: Message) -> None:
    answer = await(gpt_client.command_request('random'))
    await message.answer(answer)


@command_router.message(F.text)
async def text_handler(message: Message) -> None:
    user_id = message.from_user.id
    print(f"текст из телеги {message.text}")
    answer = await(gpt_client.text_request(user_id = user_id, text = message.text))
    print(f"ответ из чата гпт {answer}")
    await message.answer(answer)
