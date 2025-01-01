from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import sqlite3
from crud_functions import *

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

get_all_products()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()
    activity = State()


button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
button_12 = InlineKeyboardButton(text='Купить', callback_data='Купить')
kb_cal = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_1, button_2).add(button_12)

b_pr_1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
b_pr_2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
b_pr_3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
b_pr_4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
b_pr_5 = InlineKeyboardButton(text='Product5', callback_data='product_buying')

kb_prod = InlineKeyboardMarkup(resize_keyboard=True).row(b_pr_1, b_pr_2, b_pr_3, b_pr_4, b_pr_5)


@dp.callback_query_handler(text='Купить')
async def get_buying_list(call):
    products = cursor.fetchall()
    for product in products:
        await call.message.answer(f'Название: {product[1]}| Описание: {product[2]} | Цена: {product[3]}')
        with open(f"{product[0]}.png", "rb") as img:
            await call.message.answer_photo(img)
    await call.message.answer(f"Выберите продукт для покупки:", reply_markup=kb_prod)
    await call.answer()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(f"Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(text='start')
async def main_menu(call):
    await call.message.answer(
        f"Привет {call.message.from_user.username}! Я бот помогающий твоему здоровью.\nВыберите опцию:",
        reply_markup=kb_cal)
    await call.answer()


button_10 = InlineKeyboardButton(text='Фомула', callback_data='form')
button_11 = InlineKeyboardButton(text='Дополнительная информация', callback_data='info')
kb_info = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_10, button_11)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("Формулы расчёта", reply_markup=kb_info)
    await call.answer()


@dp.callback_query_handler(text='form')
async def get_formulas(call):
    await call.message.answer(
        'для женщины: 10 * вес(кг) + 6.25 * рост (см) – 4.92 * возраст – 161\nдля мужчины: 10 * вес (кг) + 6.25 * рост (см) – 4.92 * возраст + 5')
    await call.answer()


@dp.callback_query_handler(text='info')
async def get_info(call):
    await call.message.answer(
        'Формула Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для оптимального похудения или сохранения нормального веса. Она была выведена в 2005 году и все чаще стала заменять классическую формулу Харриса-Бенедикта.'
        '\nhttps://www.calc.ru/Formula-Mifflinasan-Zheora.html')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите пожалуйста свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Укажите свой рост в сантиметрах:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


button_3 = InlineKeyboardButton(text='Мужской', callback_data='m')
button_4 = InlineKeyboardButton(text='Женский', callback_data='f')
kb_sex = InlineKeyboardMarkup(resize_keyboard=True).row(button_3, button_4)


@dp.message_handler(state=UserState.weight)
async def set_sex(message, state):
    await state.update_data(weight=message.text)
    await message.answer("Ваш пол:", reply_markup=kb_sex)
    await UserState.sex.set()


button_5 = InlineKeyboardButton(text='1', callback_data='1')
button_6 = InlineKeyboardButton(text='2', callback_data='2')
button_7 = InlineKeyboardButton(text='3', callback_data='3')
button_8 = InlineKeyboardButton(text='4', callback_data='4')
button_9 = InlineKeyboardButton(text='5', callback_data='5')
kb_activity = InlineKeyboardMarkup(resize_keyboard=True).row(button_5, button_6, button_7,
                                                             button_8, button_9)


@dp.callback_query_handler(state=UserState.sex)
async def set_activity(message, state):
    # await call.answer()
    await state.update_data(sex=message.data)
    await message.message.answer(
        "Ваша повседневная физическая активности от 1 до 5\n, где \n1 - минимальная активность\n2 - слабая активность\n3 - средняя активность\n4 - высокая активность\n5 - экстра-активност",
        reply_markup=kb_activity)
    await message.answer()
    await UserState.activity.set()


@dp.callback_query_handler(state=UserState.activity)
async def send_calories(message, state):
    await state.update_data(activity=message.data)
    data = await state.get_data()
    # await message.answer(
    #     f"{data['activity']} | {data['sex']}")
    A = [1.2, 1.375, 1.55, 1.725, 1.9]
    if data['sex'] == 'm':
        Cals = ((10.0 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5.0 * float(data['age'])) + 5.0) * (
            A[int(data['activity']) - 1])
    else:
        Cals = ((10.0 * float(data['weight'])) + (6.25 * float(data['growth'])) - (
                5.0 * float(data['age'])) - 161.0) * (A[int(data['activity']) - 1])
    await message.message.answer(
        f'Ваша норма килокалорий в сутки: {round(Cals, 2)} ккал')
    await message.answer()
    await state.finish()


button_0 = InlineKeyboardButton('СТАРТ', callback_data='start')
kb_start = InlineKeyboardMarkup(resize_keyboard=True).add(button_0)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.', reply_markup=kb_start)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
