import logging
import math22
import math
import requests
import random
from aiogram import Bot, Dispatcher, executor, types
from sqliter import SQLighter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# db = SQLighter("db2.db")
user_dictionary = dict()


def make_all_functions_inactive():
    weather.wind = False
    weather.temperature = False
    math_func.fib = False
    math_func.prime = False
    math_func.square = False
    math_func.convert = False
    math_games.game = False


class MathFunctions:
    def __init__(self, fib, prime, square, convert):
        self.fib = fib
        self.prime = prime
        self.square = square
        self.convert = convert


class MathGames:
    def __init__(self, game, counter, random_number):
        self.game = game
        self.counter = counter
        self.random_number = random_number


class WeatherForeCast:
    def __init__(self, temperature, wind):
        self.temperature = temperature
        self.wind = wind


math_func = MathFunctions(False, False, False, False)
math_games = MathGames(False, 0, 0)
weather = WeatherForeCast(False, False)
bot = Bot(token='1068750481:AAGym-mE8kWJTunTVrXhp0_CNd4_XErgGLM')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    # if not db.subscriber_exists(message.from_user.username):
    #     db.add_subscriber(message.from_user.username)
    # else:
    #     db.update_subscription(message.from_user.username, True)
    #     print("User name is exist")
    user_dictionary[message.from_user.id] = "Username: @" + str(message.from_user.username) + ", first_name: " + str(
        message.from_user.first_name) + ", last_name: " + str(message.from_user.last_name)
    print(user_dictionary)
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
    make_all_functions_inactive()
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Contact", url='https://t.me/sasha_reshetar'))
    await message.answer("If you have any questions, please contact me", parse_mode='html', reply_markup=markup)


@dp.message_handler(commands='website')
async def open_site(message: types.Message):
    make_all_functions_inactive()
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Visit", url='https://chess32x64.org'))
    await message.answer("Great! This is website of my chess club😁", parse_mode='html', reply_markup=markup)


@dp.message_handler(commands='followers')
async def show_followers(message: types.Message):
    if message.from_user.username is not None:
        if message.from_user.username == "sasha_reshetar":
            await message.answer(str(user_dictionary))
    await message.answer(str(len(user_dictionary)))


@dp.message_handler(text='Menu')
async def show_main_menu(message: types.Message):
    make_all_functions_inactive()
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
    make_all_functions_inactive()
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
    make_all_functions_inactive()
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

    btns_text = ('Fibonacci', 'isPrime', 'Game')
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
    make_all_functions_inactive()
    math_func.fib = True
    await message.answer("Give number, and I will return n-th fibonacci")


@dp.message_handler(text="Convert")
async def convert_func(message: types.Message):
    make_all_functions_inactive()
    math_func.convert = True
    await message.answer("Give base source, base destination and number, using format: 62 10 536")


@dp.message_handler(text="Temperature")
async def show_temperature(message: types.Message):
    make_all_functions_inactive()
    weather.temperature = True
    await message.answer("Tell me city, and I will say its temperature")


@dp.message_handler(text="Wind")
async def show_wind(message: types.Message):
    make_all_functions_inactive()
    weather.wind = True
    await message.answer("Tell me city, and I will say its wind speed")


@dp.message_handler(text="isPrime")
async def is_prime(message: types.Message):
    make_all_functions_inactive()
    math_func.prime = True
    await message.answer("Give number, and I will say if its prime")


@dp.message_handler(text="Game")
async def play_game(message: types.Message):
    make_all_functions_inactive()
    math_games.game = True
    math_games.counter = 0
    math_games.random_number = random.randint(0, 100)
    await message.answer("Guess number, you have 7 tries")


@dp.message_handler(text="isSquare")
async def is_square(message: types.Message):
    make_all_functions_inactive()
    math_func.square = True
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
    elif math_games.game:

        try:
            if int(message.text) > math_games.random_number:
                math_games.counter += 1
                if math_games.counter != 7:
                    await message.answer("Try less number")

            elif int(message.text) < math_games.random_number:
                math_games.counter += 1
                if math_games.counter != 7:
                    await message.answer("Try greater number")

            else:
                math_games.counter += 1
                await message.answer("Correct!👍, you guessed for " + str(math_games.counter) + " tries")
                math_games.counter = 0
                math_games.game = False
            if math_games.counter == 7:
                await message.answer("You lost😱")
                math_games.game = False
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
