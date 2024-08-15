import asyncio
from aiogram import F, Router
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums import ChatAction

import app.keyboards as kb

router = Router()

class Reg(StatesGroup):
    name = State()
    phone_number = State()


@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.bot.send_chat_action(chat_id=msg.from_user.id,
                                       action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await msg.reply(f"Привет!\n твой id: {msg.from_user.id} Имя: {msg.from_user.first_name}",
                    reply_markup=kb.main)

@router.message(Command('get'))
async def cmd_get(message: Message, command: CommandObject):
    if not command.args:
        await message.answer('Аргументы не переданы')
        return
    try:
        value1, value2 = command.args.split(' ', maxsplit=1)
        await message.answer(f'Вы ввели команду get с аргументом {value1} {value2}')
    except:
        await message.answer('Были введены неправильные аргументы')

@router.message(Command("help"))
async def get_help(msg: Message):
    await msg.answer("Комманда help")

@router.message(F.contact)
async def get_help(msg: Message):
    print(msg.contact.phone_number)
    await msg.answer("Телефон получен")

@router.message(F.text == "Как дела?")
async def whats_up(msg: Message):
    await msg.answer("ОК")

@router.message(Command("photo"))
async def cmd_start(message: Message):
    await message.reply('Привет!')
    await message.answer_photo(photo='https://sudoteach.com/static/assets/img/aiogram-banner.jpg',
                               caption='Лучший курс по aiogram!')

@router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог', show_alert=True)
    await callback.message.edit_text("Вот наш каталог!", reply_markup=await kb.brands())

@router.callback_query(F.data == 'basket')
async def basket(callback: CallbackQuery):
    await callback.answer('Вы выбрали корзину', show_alert=True)
    await callback.message.answer('Ваша корзина пуста.')

@router.message(Command("reg"))
async def reg_first(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Введите Ваше имя")

@router.message(Reg.name)
async def reg_second(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.phone_number)
    await message.answer("Введите Ваш номер телефона")

@router.message(Reg.phone_number)
async def reg_third(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    data = await state.get_data()
    await message.answer(f"Регистрация завершена\nИмя: {data["name"]} \nНомер телефона: {data["phone_number"]}")
    await state.clear()