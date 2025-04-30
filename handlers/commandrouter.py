from aiogram import Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from classes import gpt_client


command_router = Router()

@command_router.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Gre loves, {message.from_user.full_name}!")

@command_router.message(Command('random'))
async def command_random_handler(message: Message) -> None:
    answer = await(gpt_client.text_request('random') )
    await message.answer(answer)



# @dp.message(Command('gpt'))
# async def command_random_handler(message: Message) -> None:
#     await gpt_client.text_request('message')
#
#
# @dp.message(F.text)
# async def text_handler(message: Message) -> None:
#     response = client.responses.create(
#         model="gpt-4o-mini-2024-07-18",
#         input=str(message),
#         instructions="Разговаривай как молодой влюбленные поэт"
#     )
#     await message.answer(f"{response.output_text}")
