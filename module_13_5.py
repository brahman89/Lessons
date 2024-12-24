from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()
    activity = State()


button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_1, button_2)


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")
    await asyncio.sleep(1)
    await message.answer("Предлагаю Вам рассчитать на себе  формулу 'Миффлина-Сан Жеора'")
    await asyncio.sleep(1)
    await message.answer(
        "Для получения дополнительной информации введите: 'Информация' \nДля участия введите: 'Рассчитать'",
        reply_markup=kb)


@dp.message_handler(text=['Информация'])
async def set_age(message):
    await message.answer(
        'Формула Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для оптимального похудения или сохранения нормального веса. Она была выведена в 2005 году и все чаще стала заменять классическую формулу Харриса-Бенедикта.'
        '\nhttps://www.calc.ru/Formula-Mifflinasan-Zheora.html')


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите пожалуйста свой возраст:')
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


button_3 = KeyboardButton(text='m')
button_4 = KeyboardButton(text='f')
kb_sex = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_3, button_4)


@dp.message_handler(state=UserState.weight)
async def set_sex(message, state):
    await state.update_data(weight=message.text)
    await message.answer("Пожалуста укажите свой пол:\nмужской - 'm'\nженский - 'f'", reply_markup=kb_sex)
    await UserState.sex.set()


button_5 = KeyboardButton(text='1')
button_6 = KeyboardButton(text='2')
button_7 = KeyboardButton(text='3')
button_8 = KeyboardButton(text='4')
button_9 = KeyboardButton(text='5')
kb_activity = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_5, button_6, button_7,
                                                                                    button_8, button_9)


@dp.message_handler(state=UserState.sex)
async def set_activity(message, state):
    await state.update_data(sex=message.text)
    await message.answer(
        "Оцените и укажите степень повседневной своей физической активности от 1 до 5\n, где \n1 - минимальная активность\n2 - слабая активность\n3 - средняя активность\n4 - высокая активность\n5 - экстра-активност", reply_markup=kb_activity)
    await UserState.activity.set()


@dp.message_handler(state=UserState.activity)
async def send_calories(message, state):
    await state.update_data(activity=message.text)
    data = await state.get_data()
    # await message.answer(
    #     f"{data['weight'], data['growth'], data['age'], data['activity'], data['sex']}")
    A = [1.2, 1.375, 1.55, 1.725, 1.9]
    if data['sex'] == 'm':
        Cals = ((10.0 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5.0 * float(data['age'])) + 5.0) * (
            A[int(data['activity']) - 1])
    else:
        Cals = ((10.0 * float(data['weight'])) + (6.25 * float(data['growth'])) - (
                5.0 * float(data['age'])) - 161.0) * (A[int(data['activity']) - 1])
    await message.answer(
        f'Необходимое количество килокалорий в сутки равно:\n{round(Cals, 2)} ккал')

    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
