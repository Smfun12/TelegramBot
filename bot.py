import logging
import weather_reporter
import weather_forcaster
# import requests
import math22
import COVID19Py
from aiogram import Bot, Dispatcher, md, executor, types

# covid = COVID19Py.COVID19()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class bolleans:
    def __init__(self, fib, prime, square):
        self.fib = fib
        self.prime = prime
        self.square = square


x = bolleans(False, False, False)
bot = Bot(token='1068750481:AAGym-mE8kWJTunTVrXhp0_CNd4_XErgGLM')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    # default row_width is 3, so here we can omit it actually
    # kept for clearness

    btns_text = ('Fibonacci', "")
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    # adds buttons as a new row to the existing keyboard
    # the behaviour doesn't depend on row_width attribute

    more_btns_text = (
        "isPrime",
        "isSquare"
    )
    keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))
    # adds buttons. New rows are formed according to row_width parameter

    await message.reply("Hi!\nWhat do you want to do?", reply_markup=keyboard_markup)


#
# @dp.message_handler(commands="start")
# async def weather(message: types.Message):
#     await message.answer(covid.getLatestChanges())
#
#
@dp.message_handler(text="Fibonacci")
async def is_fib(message: types.Message):
    x.fib = True
    x.prime = False
    x.square = False
    await message.answer("Give number, i return n-th fibonacci")


@dp.message_handler(text="isPrime")
async def is_prime(message: types.Message):
    x.prime = True
    x.fib = False
    x.square = False
    await message.answer("Give number, i say if its prime")


@dp.message_handler(text="isSquare")
async def is_square(message: types.Message):
    x.square = True
    x.prime = False
    x.fib = False
    await message.answer("Give number, i say if its square")


@dp.message_handler()
async def hello(message: types.Message):
    if x.fib:

        try:
            await message.answer("Here it is: " + str(math22.fib(int(message.text))))
        except ValueError:
            await message.answer("Enter integer")
    elif x.prime:

        try:
            await message.answer("Here it is: " + str(math22.is_prime(int(message.text))))
        except ValueError:
            await message.answer("Enter integer")
    elif x.square:

        try:
            await message.answer("Here it is: " + str(math22.is_square(int(message.text))))
        except ValueError:
            await message.answer("Enter integer")
    else:

        await message.answer(message.text)


#
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
