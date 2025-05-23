from aiogram import Router

from .commandrouter import command_router

main_router = Router()
main_router.include_routers(
    command_router,
)

__all__ = [
    'main_router',
]