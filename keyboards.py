from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboard_dinner_room = [
    [KeyboardButton(text="Столовая 7")],
    [KeyboardButton(text="Столовая 8")],
    [KeyboardButton(text="Столовая 40")],
    [KeyboardButton(text="Столовая КИЦ")],
    [KeyboardButton(text="Столовая КОП")]
]
kb_dinner_room = ReplyKeyboardMarkup(keyboard =keyboard_dinner_room)


keyboard_main_menu = [
    [KeyboardButton(text="Личный кабинет")],
    [KeyboardButton(text="Режим работы")],
    [KeyboardButton(text="Расписание блюд на сегодня")],
    [KeyboardButton(text="Книга жалоб и предложений")],
    [KeyboardButton(text="Сообщить об ошибке в работе бота")]
]
kb_main_menu = ReplyKeyboardMarkup(keyboard =keyboard_main_menu)