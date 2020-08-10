import logging
import math22
import math
import requests

from aiogram import Bot, Dispatcher, executor, types
from sqliter import SQLighter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

db = SQLighter("db2.db")


class MathFunctions:
    def __init__(self, fib, prime, square, convert):
        self.fib = fib
        self.prime = prime
        self.square = square
        self.convert = convert


class WeatherForeCast:
    def __init__(self, temperature, wind):
        self.temperature = temperature
        self.wind = wind


math_func = MathFunctions(False, False, False, False)
weather = WeatherForeCast(False, False)
bot = Bot(token='1068750481:AAGym-mE8kWJTunTVrXhp0_CNd4_XErgGLM')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    if not db.subscriber_exists(message.from_user.username):
        db.add_subscriber(message.from_user.username)
    else:
        db.update_subscription(message.from_user.username, True)

    math_func.fib = False
    math_func.prime = False
    math_func.square = False
    math_func.convert = False
    weather.temperature = False
    weather.wind = False
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1)
    # default row_width is 3, so here we can omit it actually
    # kept for clearness

    btns_text = ('Math functions', '')
    more_btns_text = (
        "Weather", ""
    )
    keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    # adds buttons as a new row to the existing keyboard
    # the behaviour doesn't depend on row_width attribute

    # adds buttons. New rows are formed according to row_width parameter

    await message.reply("Hi!\nWhat do you want to do?", reply_markup=keyboard_markup)


@dp.message_handler(commands='help')
async def show_me(message: types.Message):
    math_func.fib = False
    math_func.prime = False
    math_func.square = False
    math_func.convert = False
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Contact", url='https://t.me/sasha_reshetar'))
    await message.answer("If you have any questions, please contact me", parse_mode='html', reply_markup=markup)


@dp.message_handler(commands='website')
async def open_site(message: types.Message):
    math_func.fib = False
    math_func.prime = False
    math_func.square = False
    math_func.convert = False
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Visit", url='https://chess32x64.org'))
    await message.answer("Great! This is website of my chess club😁", parse_mode='html', reply_markup=markup)


@dp.message_handler(text='Menu')
async def show_main_menu(message: types.Message):
    weather.wind = False
    weather.temperature = False
    math_func.fib = False
    math_func.prime = False
    math_func.square = False
    math_func.convert = False
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1)
    # default row_width is 3, so here we can omit it actually
    # kept for clearness

    btns_text = ('Math functions', '')
    more_btns_text = (
        "Weather", ""
    )
    keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    # adds buttons as a new row to the existing keyboard
    # the behaviour doesn't depend on row_width attribute

    # adds buttons. New rows are formed according to row_width parameter

    await message.reply("Hi again😊 ", reply_markup=keyboard_markup)


@dp.message_handler(text="Weather")
async def weather_menu(message: types.Message):
    math_func.fib = False
    math_func.prime = False
    math_func.square = False
    math_func.convert = False
    weather.temperature = False
    weather.wind = False
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1)

    btns_text = ('Temperature', '')
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    more_btns_text = (
        "Wind",
        "Menu"
    )
    keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))

    await message.answer("Choose one", reply_markup=keyboard_markup)


@dp.message_handler(text="Math functions")
async def math_functions_menu(message: types.Message):
    math_func.fib = False
    math_func.prime = False
    math_func.square = False
    math_func.convert = False
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)

    btns_text = ('Fibonacci', 'isPrime')
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    more_btns_text = (
        "isSquare",
        "Convert",
        'Menu'
    )
    keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))

    await message.answer("Choose one", reply_markup=keyboard_markup)


@dp.message_handler(text="Fibonacci")
async def is_fib(message: types.Message):
    math_func.fib = True
    math_func.prime = False
    math_func.square = False
    math_func.convert = False
    weather.temperature = False
    weather.wind = False
    await message.answer("Give number, and I will return n-th fibonacci")


@dp.message_handler(text="Convert")
async def convert_func(message: types.Message):
    math_func.convert = True
    math_func.fib = False
    math_func.prime = False
    math_func.square = False
    weather.temperature = False
    weather.wind = False
    await message.answer("Give base source, base destination and number, using format: 62 10 536")


@dp.message_handler(text="Temperature")
async def show_temperature(message: types.Message):
    weather.temperature = True
    weather.wind = False
    math_func.prime = False
    math_func.fib = False
    math_func.square = False
    math_func.convert = False
    await message.answer("Tell me city, and I will say its temperature")


@dp.message_handler(text="Wind")
async def show_wind(message: types.Message):
    weather.temperature = False
    weather.wind = True
    math_func.prime = False
    math_func.fib = False
    math_func.square = False
    math_func.convert = False
    await message.answer("Tell me city, and I will say its wind speed")


@dp.message_handler(text="isPrime")
async def is_prime(message: types.Message):
    math_func.prime = True
    math_func.fib = False
    math_func.square = False
    math_func.convert = False
    weather.temperature = False
    weather.wind = False
    await message.answer("Give number, and I will say if its prime")


@dp.message_handler(text="isSquare")
async def is_square(message: types.Message):
    math_func.square = True
    math_func.prime = False
    math_func.fib = False
    math_func.convert = False
    weather.temperature = False
    weather.wind = False
    await message.answer("Give number, and I will say if its square")


@dp.message_handler()
async def hello(message: types.Message):
    show_weather = True
    temperature = ""
    wind_speed = ""
    if weather.temperature or weather.wind:

        city = str(message.text).lower()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2466a1390232dc745e20075185ca0326&units=metric'.format(
            city)
        res = requests.get(url)
        data = res.json()
        try:
            temp = data['main']['temp']
            temperature = str(temp)
            wind_velocity = data['wind']['speed']
            wind_speed = str(wind_velocity)
        except KeyError:
            show_weather = False
            await message.answer("Enter existing city")
    if math_func.fib:

        try:
            await message.answer("Here it is: " + str(math22.fib(int(message.text))))
        except ValueError:
            await message.answer("Enter integer")
    elif math_func.convert:
        string = str(message.text).split()
        try:

            await message.answer(
                "Here it is: " + str(math22.base_convert(int(string[0]), int(string[1]), int(string[2]))))
        except Exception:
            await message.answer(
                "Use valid format!")
    elif math_func.prime:

        try:
            if int(message.text) > 1:
                await message.answer("Here it is: " + str(math22.is_prime(int(message.text))))
            elif int(message.text) == 1:
                await message.answer("1 is not prime by default")
            else:
                await message.answer("0 or less cannot be prime")
        except ValueError:
            await message.answer("Enter integer")
    elif math_func.square:

        try:
            if int(message.text) >= 0:
                temp = math22.is_square(int(message.text))
                if temp:
                    await message.answer("Here it is: " + str(math22.is_square(int(message.text))) + ", result " + str(
                        int(math.sqrt(int(message.text)))))
                else:
                    await message.answer("Here it is: " + str(math22.is_square(int(message.text))))
            else:
                await message.answer("Number cannot be < 0")
        except ValueError:
            await message.answer("Enter integer")
    elif weather.temperature:
        if show_weather:
            await message.answer("Here is it: " + temperature + " °C")
    elif weather.wind:
        if show_weather:
            await message.answer("Here is it: " + wind_speed + " meter/sec")
    else:
        await message.answer("Your text: " + str(message.text))


#
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
