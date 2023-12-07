from aiogram.fsm.state import State, StatesGroup
from aiogram import Bot

bottoken ="PASTE YOUR TOKEN"
bot = Bot(token=bottoken)

class Form(StatesGroup):
    main = State()
    getimage = State()
    resizearg = State()
    rotatearg = State()
    sharpenarg = State()
    brightarg = State()
    contrastarg = State()

class Strings:
    start = """Привет! Этот бот редактирует изображения.
Для начала дайте боту фотографию прописав /get
Для подробной информации о командах пропишите /help
"""
    help = f"""Команды:
/get — Дать боту изображение для редактирования.
/resize — Изменить размер изображения.
/discolor — Обесцветить изображение.
/blur — Слегка замылить изображение.
/reverse — Инвертировать цвета изображения.
/edges — Выделить края.
/rotate — Повернуть изображение.
/sharpen — Повысить резкость.
/bright — Затемнить.
/contrast — Повысить контрастность."""