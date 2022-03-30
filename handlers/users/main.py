from aiogram import types
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import ContentType

from __main__ import main_router
from keyboards.default.main_kb import MainMenuKb, MainMenuBtn
from loader_db import groups_db, parameter_str_db
from states.state import MainMenuState


@main_router.message(lambda message: message.chat.type == 'private', commands=('start',))
async def start_commands(message: types.Message):
    await message.answer(
        text="Спам бот",
        reply_markup=MainMenuKb.main_menu()
    )


@main_router.message(lambda message: message.chat.type == 'private' and message.text == MainMenuBtn.see_groups)
async def see_groups_btn(message: types.Message):
    text = "Список всіх груп, в яких знаходится спам бот\n\n"
    for name_group in groups_db.get_all_id_groups('`name`'):
        text += f'{name_group}\n'

    await message.answer(text=text)


@main_router.message(lambda message: message.chat.type == 'private' and message.text == MainMenuBtn.add_text)
async def add_text_btn(message: types.Message, state: FSMContext):
    text = "Напишіть текст, який ви хочете, щоб надсилався в чати"
    await message.answer(text=text, reply_markup=MainMenuKb.back())

    await state.set_state(MainMenuState.add_text)


@main_router.message(lambda message: message.chat.type == 'private' and message.text == MainMenuBtn.back,
                     state=MainMenuState.add_text)
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await start_commands(message=message)


@main_router.message(lambda message: message.chat.type == 'private', content_types=ContentType.TEXT,
                     state=MainMenuState.add_text)
async def add_text_btn(message: types.Message, state: FSMContext):
    parameter_str_db.exists_and_update_or_add('send_message', message.text)
    text = "Змінено текст"
    await message.reply(text=text)
    await back_to_main_menu(message=message, state=state)
