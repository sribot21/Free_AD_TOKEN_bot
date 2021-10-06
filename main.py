import os
import telebot


bot = telebot.Telebot("2097395997:AAGieE29KKlcAWKoq2It2KoG1LsVaGPj10o")


@bot.message_handler(commands=["start"])
def send_welcome(message):
bot.reply_to(message, "Hello! I'm ad token Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message)
bot.send_message(message, "https://www.youtube.com/channel/UCasEPrsQWCgrTl8g6OpAuJw")


bot.polling() 

