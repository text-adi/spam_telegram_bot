from aiogram.dispatcher.filters.state import StatesGroup, State


class MainMenuState(StatesGroup):
    add_text = State()
