import telebot
import requests
import random
from bs4 import BeautifulSoup

token = '5970338062:AAFyaQrC1nKmh9wraAWh0jObxslPAzAUJis'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["audio"])
def send_audio(message):
    audio = open("happy.mp3","rd")
    bot.send_audio(message.chat.id,audio)

def new_func():
    audio = open("happy.mp3","rd")
    return audio

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("Факт")
    button2 = telebot.types.KeyboardButton("Котики")
    button3 = telebot.types.KeyboardButton("Стихотворение")
    button4 = telebot.types.KeyboardButton("Аудио")
    button5 = telebot.types.KeyboardButton("Во что поиграть на компьютере?")
    keyboard.add(button1,button2,button3,button4,button5)
    bot.send_message(message.chat.id,  welcome_text,reply_markup=keyboard)

@bot.message_handler(cotnent_types=["text"])
def answer(message):
    if message.text == "Факт":
        send_fact(message)
    elif message.text == "Котики":
        send_cat(message)
    elif message.text == "Стихотворение":
        send_poem(message)
    elif message.text == "Аудио":
        send_audio(message)
    elif message.text == "Во что поиграть на компьютере?":
        send_game(message)
    #elif message.text == "Стикер":
        #send_sticker(message)


@bot.message_handler(commands=['game'])
def send_game(message):
    game =  "The Elder Scrolls 5:Skyrim, Grand Theft Auto 5, Minecraft"
    keyboard =  telebot.types.InlineKeyboardMarkup()
    button_5 = telebot.types.InlineKeyboardButton
    keyboard.add(button_5)
    bot.send_game(message.chat.id, game.text.strip(), reply_markup=keyboard)


@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)

@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link =  fact.a.attrs['href']
    keyboard =  telebot.types.InlineKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton("Перейти",url=fact_link)
    keyboard.add(button_1)
    bot.send_fact(message.chat.id, fact.text.strip(), reply_markup=keyboard)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1,10))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

bot.polling()

