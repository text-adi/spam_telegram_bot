from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class MainMenuBtn:
    add_text = "Додати текст"
    see_groups = "Переглянути всі всі доступні чати"
    back = "Відмінити"


class MainMenuKb:
    @staticmethod
    def main_menu():
        builder = ReplyKeyboardBuilder()
        for button in (MainMenuBtn.add_text, MainMenuBtn.see_groups):
            builder.add(KeyboardButton(text=button))
        builder.adjust(2)
        kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=builder.export())
        return kb

    @staticmethod
    def back():
        builder = ReplyKeyboardBuilder()
        for button in (MainMenuBtn.back,):
            builder.add(KeyboardButton(text=button))
        builder.adjust(2)
        kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=builder.export())
        return kb
