import asyncio

from aiogram import types

from __main__ import main_router
from loader_db import groups_db, parameter_bool_db, parameter_str_db


@main_router.message(content_types=['new_chat_members'])
async def welcome_chat_group(message: types.Message):
    """Якщо бота добавили в чат"""
    groups_db.group_exists_and_update_or_add(message.chat.id, message.chat.invite_link, message.chat.title)


@main_router.message(content_types=['left_chat_member'])
async def remove_chat_group(message: types.Message):
    """Якщо бота видалили з чату"""
    groups_db.group_exists_and_remove(message.chat.id)


@main_router.message(lambda message: message.forward_from_chat)
async def send_message_for_new_post(message: types.Message):
    if parameter_bool_db.exists('new_post'):
        if message.forward_from_chat.title == message.sender_chat.title:
            await message.reply(parameter_str_db.get_name('send_message'))


async def send_message_time():
    """Надсилає повідомлення через вказаний час"""
    await asyncio.sleep(5)
    while True:
        print("1")
        await asyncio.sleep(5)
