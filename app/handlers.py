
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.reply(f"Привет!\n твой id: {msg.from_user.id} Имя: {msg.from_user.first_name}", reply_markup=kb.main)

@router.message(Command("help"))
async def get_help(msg: Message):
    await msg.answer("Комманда help")

@router.message(F.text == "Как дела?")
async def whats_up(msg: Message):
    await msg.answer("ОК")