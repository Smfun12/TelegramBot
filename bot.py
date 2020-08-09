import logging
import math22

from aiogram import Bot, Dispatcher, md, executor, types

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class bolleans:
    def __init__(self, fib, prime, square, convert):
        self.fib = fib
        self.prime = prime
        self.square = square
        self.convert = convert


x = bolleans(False, False, False, False)
bot = Bot(token='1068750481:AAGym-mE8kWJTunTVrXhp0_CNd4_XErgGLM')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    x.fib = False
    x.prime = False
    x.square = False
    x.convert = False
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    # default row_width is 3, so here we can omit it actually
    # kept for clearness

    btns_text = ('Fibonacci', "Convert")
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


@dp.message_handler(commands='help')
async def show_me(message: types.Message):
    x.fib = False
    x.prime = False
    x.square = False
    x.convert = False
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Contact", url='https://t.me/sasha_reshetar'))
    await message.answer("If you have any questions, please contact me", parse_mode='html', reply_markup=markup)


@dp.message_handler(commands='website')
async def open_site(message: types.Message):
    x.fib = False
    x.prime = False
    x.square = False
    x.convert = False
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Visit", url='https://chess32x64.org'))
    await message.answer("Great! This is website of my chess club", parse_mode='html', reply_markup=markup)


@dp.message_handler(text="Fibonacci")
async def is_fib(message: types.Message):
    x.fib = True
    x.prime = False
    x.square = False
    x.convert = False
    await message.answer("Give number, i return n-th fibonacci")


@dp.message_handler(text="Convert")
async def convert(message: types.Message):
    x.convert = True
    x.fib = False
    x.prime = False
    x.square = False
    await message.answer("Give base source, base destination and number, using format: 62 10 536")


@dp.message_handler(text="isPrime")
async def is_prime(message: types.Message):
    x.prime = True
    x.fib = False
    x.square = False
    x.convert = False
    await message.answer("Give number, and I will say if its prime")


@dp.message_handler(text="isSquare")
async def is_square(message: types.Message):
    x.square = True
    x.prime = False
    x.fib = False
    x.convert = False
    await message.answer("Give number, and I will say if its square")


@dp.message_handler()
async def hello(message: types.Message):
    if x.fib:

        try:
            await message.answer("Here it is: " + str(math22.fib(int(message.text))))
        except ValueError:
            await message.answer("Enter integer")
    elif x.convert:
        string = str(message.text).split()
        try:

            await message.answer(
                "Here it is: " + str(math22.base_convert(int(string[0]), int(string[1]), int(string[2]))))
        except Exception:
            await message.answer(
                "Use valid format!")
    elif x.prime:

        try:
            if int(message.text) > 1:
                await message.answer("Here it is: " + str(math22.is_prime(int(message.text))))
            elif int(message.text) == 1:
                await message.answer("1 is not prime by default")
            else:
                await message.answer("0 or less cannot be prime")
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
