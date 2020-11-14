from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from defs import *
# from aiogram.api.methods import SendSticker
import mysql.connector


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()
    Q8 = State()
    Q9 = State()
    Q10 = State()
    Q11 = State()
    Q12 = State()
    Q13 = State()

async def isolation(message):
    global symptoms
    symptoms = '-'
    # print(message)
    # await bot.send_message(message.chat.id, f"Спасибо!")
    await message.answer(text="Твоя группа на удаленке?", reply_markup=inline())
    await Test.Q6.set()


async def question2(message):
    global first_q
    first_q = '-'
    await bot.send_message(message.chat.id, f"Как дела с наукой?🔬\nЧем на данный момент занят? Что планируешь?")
    await Test.Q9.set()


async def hello(message):
    global name
    name = (message['from'])['first_name']
    print(type(message))
    global surname
    surname = (message['from'])['last_name']
    global user_id
    user_id = int(message.chat.id)
    await bot.send_message(message.chat.id, f"Привет, {name}!\nОчередной опрос сотрудников 🦾")
    await covid(message)


bot = Bot(token='1415878352:AAEIda5qJbmYNTxYLBU1LcDiTYEz64a5dHo', parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(Command("start"))
async def start_handlers(message: types.Message):
    await hello(message)


@dp.callback_query_handler(state=Test.Q4)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
# async def inlin(call: types.CallbackQuery, state: ''):
    if callback_query.data == 'yes':
        await bot.send_message(callback_query.message.chat.id, 'Напиши какие у тебя симптомы, и мы пойдем дальше?')
        await Test.Q5.set()
    elif callback_query.data == 'no':
        # await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
        await isolation(callback_query.message)


@dp.message_handler(state=Test.Q5)
async def answer_q3(message: types.Message, state:''):
    global symptoms
    symptoms = message.text
    await message.answer("Твоя группа на удаленке?", reply_markup=inline())
    await Test.Q6.set()


@dp.callback_query_handler(state=Test.Q6)
async def inlin(callback_query: types.CallbackQuery):
    global block_group
    if callback_query.data == 'yes':
        block_group = '+'
    elif callback_query.data == 'no':
        block_group = '-'
    print(block_group)
    await question1(callback_query.message)


@dp.callback_query_handler(state=Test.Q7)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
# async def inlin(call: types.CallbackQuery, state: ''):
    if callback_query.data == 'yes':
        await bot.send_message(callback_query.message.chat.id, 'Напиши какими, и на каком этапе они находятся')
        await Test.Q8.set()
    elif callback_query.data == 'no':
        await bot.send_message(callback_query.message.chat.id, 'Это надо исправлять!🤬')

        # await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
        await question2(callback_query.message)


@dp.message_handler(state=Test.Q8)
async def answer_q3(message: types.Message, state:''):
    global first_q
    first_q = message.text
    await message.answer(f"Как дела с наукой?🔬\nЧем на данный момент занят? Что планируешь?")
    await Test.Q9.set()


@dp.message_handler(state=Test.Q9)
async def answer_q3(message: types.Message, state:''):
    global second_q
    second_q = message.text
    await message.answer("Есть ли у тебя трудоустройство?(на данный момент работаешь?)", reply_markup=inline())
    await Test.Q11.set()


@dp.callback_query_handler(state=Test.Q11)
async def inlin1(callback_query: types.CallbackQuery):
    global workplace
    global graphic
    if callback_query.data == 'yes':
        workplace = '+'
        graphic = '-'
        await work_place(callback_query.message)
    elif callback_query.data == 'no':
        workplace = '-'
        graphic = '-'
        await ending(callback_query.message)


async def ending(message):
    print(user_id, name, surname, block_group, symptoms, first_q, second_q, workplace, graphic)
    try:
        insert_sql('test', ('user_id, name, surname, group_irnitu, symptoms, first_q, second_q, workplace, graphic'),
                             [user_id, name, surname, block_group, symptoms, first_q, second_q, workplace, graphic])
        await bot.send_message(message.chat.id,
                               "Спасибо! 😁\nОстались вопросы?")
        await Test.Q13.set()
    except Exception as e:
        print(e)
        await bot.send_message(message.chat.id, "⚠️Ошибка при заполнении формы, пожалуйста, пройдите регистрацию заново!⚠️ \nНажмите на /start")
        await Test.Q13.set()


async def work_place(message):
    await message.answer("Если есть возможность, отправь свой график зам. по РсП, пожалуйста."
                                            "(@pugachev1, https://vk.com/m.pugachyov2013)", reply_markup=inline1())
    await Test.Q12.set()


@dp.callback_query_handler(state=Test.Q12)
async def inlin(callback_query: types.CallbackQuery):
    global graphic
    if callback_query.data == 'yes':
        graphic = '+'
        await ending(callback_query.message)
    elif callback_query.data == 'no':
        graphic = '-'
        await ending(callback_query.message)


@dp.message_handler(state=Test.Q13)
async def answer_0o9(message: types.Message, state:''):
    quest = message.text
    print(type(quest))
    if quest.lower() == 'да' or quest.lower()  == 'yes':
        await bot.send_message(message.chat.id,
                               "Пиши 👇🏼\nTelegram: @pugachev1\nVK: https://vk.com/m.pugachyov2013")
    elif quest.lower() == 'нет' or quest.lower()  == 'no':
        await bot.send_message(message.chat.id,
                               "👌🏼")
    else:
        await bot.send_message(message.chat.id,
                               "🌝")
    await state.finish()



executor.start_polling(dp, skip_updates=True)