from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="Каталог")],
#     [KeyboardButton(text="Корзина"), KeyboardButton(text="Контакты", request_contact=True)] # request_contact важный момент
# ], resize_keyboard=True,
#     input_field_placeholder="Выберете пункт меню.")

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
    [InlineKeyboardButton(text="Корзина", callback_data='basket'), InlineKeyboardButton(text="Контакты",
                                                                                       callback_data='contacts')]
])


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Youtube", url='https://www.youtube.com/@ShadowStormlq5mwdasd')]
])


cars = ["Tesla", "BMW", "Audi", "Mersedes"]

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url="https://google.com"))
    return keyboard.adjust(2).as_markup()

data = ("Nike", "Adidas", "Reebok")

def brands():
    keyboard = ReplyKeyboardBuilder()
    for brand in data:
        keyboard.add(KeyboardButton(text=brand))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)