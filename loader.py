import settings
import telebot
from database import load_users_languages
from deemix.utils.pathtemplates import fixName

bot = telebot.TeleBot (settings.TOKEN)
load_users_languages()


