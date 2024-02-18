import telebot
from tempo import read_temp


TOKEN = "6545462037:AAEThfgpxuorzflCwQ5O78rGggJaNdP2LjU" 
MY_CHAT_ID = 825380344


bot = telebot.TeleBot(TOKEN)


def alert_message():
    message_text = "Someone in the room!"
    bot.send_message(MY_CHAT_ID, message_text)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Hello! This is smart house bot!")

@bot.message_handler(commands=['temp'])
def handle_hello(message):
    bot.reply_to(message, f"{read_temp()} C")