import settings
import telebot
from database import load_users_languages

bot = telebot.TeleBot (settings.TOKEN)
load_users_languages()
