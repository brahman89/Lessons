from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
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
    A = [1.2, 1.375, 1.55, 1.725, 1.9]


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")
    await asyncio.sleep(1)
    await message.answer("Я бот, который предлагает вам применить на себе  формулу Миффлина-Сан Жеора")
    await asyncio.sleep(1)
    await message.answer(
        "Для получения дополнительной информации о данном тесте введите /info \nДля участия в тесте введите /Calories\nУдачи!")


@dp.message_handler(commands=['info'])
async def set_age(message):
    await message.answer(
        'Формула Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для оптимального похудения или сохранения нормального веса. Она была выведена в 2005 году и все чаще стала заменять классическую формулу Харриса-Бенедикта.'
        '\nhttps://www.calc.ru/Formula-Mifflinasan-Zheora.html')


@dp.message_handler(commands=['Calories'])
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


@dp.message_handler(state=UserState.weight)
async def set_sex(message, state):
    await state.update_data(weight=message.text)
    await message.answer("Пожалуста укажите свой пол:\nмужской - 'm'\nженский - 'f'")
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_activity(message, state):
    await state.update_data(sex=message.text)
    await message.answer(
        "Оцените и укажите степень повседневной своей физической активности от 1 до 5,\n где \n1-минимальная активность\n2-слабая активность\n3-средняя активность\n4-высокая активность\n5-экстра-активность")
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
        f'Необходимое количество килокалорий в сутки равно:\n{Cals} ккал')

    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
