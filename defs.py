from keyboard import inline, inline1
from mysql_lop import mycursor, mydb
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Bot, Dispatcher, types


bot = Bot(token='', parse_mode=types.ParseMode.HTML)


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


def insert_sql(table, field, message):
    mycursor.execute(f"INSERT INTO {table}({field}) VALUE ('{message[0]}', '{message[1]}', '{message[2]}', '{message[3]}', "
                     f"'{message[4]}', '{message[5]}', '{message[6]}', '{message[7]}', '{message[8]}')")
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


async def covid(message):
    await message.answer(f"🦠")
    await message.answer(f"У тебя есть симптомы ОРВИ, короновируса?", reply_markup=inline())
    await Test.Q4.set()


async def question1(message):
    # print(message)
    # await bot.send_message(message.chat.id, f"Спасибо!")
    await message.answer("Занимаешься какими-нибудь делами Карбона?", reply_markup=inline())
    await Test.Q7.set()





