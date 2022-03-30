from aiogram import types

from __main__ import main_router


@main_router.message(lambda message: message.chat.type != 'private', state='*')
async def ignore_command(message: types.Message):
    """Ігноримо повідомлення які надсилаються в чаті загальному"""
    pass

