from aiogram import types

import config
from __main__ import main_router


def is_admin(id_user: int):
    """Переріримо чи користувач є адміном"""

    return [True if id_user in config.ADMIN_ID else False][0]


@main_router.message(lambda message: not is_admin(message.from_user.id), state='*')
async def first_command(message: types.Message):
    """Заглушка"""
    pass
