import subprocess
import os
import telebot
import settings
import translations
from downloader import download_track, search_track_by_name, give_track_data
from database import find_track, add_track, update_user_language, add_user, update_user_song_counter
import time
from telebot.types import Message
from loader import bot
from deemix.utils.pathtemplates import fixName, fixLongName

os.system ("")
STATES = set()


def download_and_send(unique_id, chat_id):
    try:
        all_data = give_track_data(int(unique_id))
        track_id = find_track(name=all_data[0], album=all_data[2], artist=all_data[1])
        if track_id:
            bot.send_audio(chat_id, track_id[0])
            return
        download_track(settings.DEEZER_SONG_PRELINK + unique_id)
        file_name = str(unique_id)
        if os.path.exists('data/' + file_name + '.mp3'):
            new_audio = bot.send_audio(chat_id, open('data/' + file_name + '.mp3', 'rb'))
            try:
                if chat_id not in settings.ADMINS:
                    msg = bot.forward_message(settings.GROUPS_ID[0], chat_id, new_audio.id)
                    file_id = msg.audio.file_id
                else:
                    destination = settings.GROUPS_ID[settings.ADMINS_DESTINATION[str(chat_id)]]
                    msg = bot.forward_message(destination, chat_id, new_audio.id)
                    file_id = msg.audio.file_id
                if file_id:
                    add_track(int(unique_id), all_data[0], all_data[1], all_data[2], file_id)
            except:
                    pass
            os.remove('data/' + file_name + '.mp3')
        else:
            bot.send_message(chat_id, translations.MT [7] [translations.UL[str(chat_id)]])
    except:
        print ('\x1b[0;30;41m' + "Error in download_and_send() !" + '\x1b[0m')


@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    try:
        cursel = (call.data[1:])
        user = str(call.message.chat.id)
        
        if call.data[0] == 'S':
            download_and_send(cursel, call.message.chat.id)

        elif call.data[0] == 'L':
            translations.UL.update({user: int(cursel)})
            bot.edit_message_text(translations.CL[int(cursel)], call.message.chat.id, call.message.id)
            update_user_language(call.message.chat.id, cursel)
            
        elif call.data [0] == 'G':
            settings.ADMINS_DESTINATION.update ({user: cursel})
            bot.edit_message_text(translations.MT [10] [translations.UL[user]] + settings.GROUPS_ID_NAMES [settings.ADMINS_DESTINATION [user]], call.message.chat.id, call.message.id)
    except:
        print ('\x1b[0;30;41m' + "Error in call_handler() !" + '\x1b[0m')


@bot.message_handler(commands=['group'])
def g_get(message: Message):
    try:
        if message.chat.id in settings.ADMINS:
            user_lang = translations.UL[str(message.chat.id)]
            bot.send_message(message.chat.id, translations.MT[9][user_lang] + settings.GROUPS_ID_NAMES [settings.ADMINS_DESTINATION[str(message.chat.id)]]) #?
    except:
        print ('\x1b[0;30;41m' + "Error in g_get() !" + '\x1b[0m')


@bot.message_handler(commands=['switch'])
def g_switch(message: Message):
    try:
        if message.chat.id in settings.ADMINS:
            markup = telebot.types.InlineKeyboardMarkup()
            for i in settings.GROUPS_ID_NAMES:
                markup.add(telebot.types.InlineKeyboardButton(settings.GROUPS_ID_NAMES[i], callback_data='G' + str(i)))
    except:
        print ('\x1b[0;30;41m' + "Error in g_switch() !" + '\x1b[0m')


@bot.message_handler(commands=['lang'])
def lang(message: Message):
    try:
        if message.chat.id in STATES:
            STATES.remove(message.chat.id)
        user_lang = translations.UL[str(message.chat.id)]

        markup = telebot.types.InlineKeyboardMarkup()
        for i in range(len(translations.LGS)):
            markup.add(telebot.types.InlineKeyboardButton(translations.LGS[i], callback_data='L' + str(i)))

        bot.send_message(message.chat.id, translations.MT[6][user_lang], reply_markup=markup)
    except:
        print ('\x1b[0;30;41m' + "Error in lang() !" + '\x1b[0m')


@bot.message_handler(commands=['search'])
def search(message: Message):
    try:
        if message.chat.id in STATES:
            STATES.remove(message.chat.id)
        user_lang = translations.UL[str(message.chat.id)]

        bot.send_message(message.chat.id, translations.MT[2][user_lang])
        STATES.add(message.chat.id)
    except:
        print ('\x1b[0;30;41m' + "Error in search() !" + '\x1b[0m')


@bot.message_handler(commands=['help'])
def helpp(message: Message):
    try:
        if message.chat.id in STATES:
            STATES.remove(message.chat.id)
        user_lang = translations.UL[str(message.chat.id)]
        if message.chat.id in settings.ADMINS:
            bot.send_message(message.chat.id, translations.MT[8][user_lang])
        else:
            bot.send_message(message.chat.id, translations.MT[1][user_lang])
    except:
        print ('\x1b[0;30;41m' + "Error in helpp() !" + '\x1b[0m')


@bot.message_handler(commands=['start'])
def start(message: Message):
    try:
        if message.chat.id in STATES:
            STATES.remove(message.chat.id)
        user_id = str(message.chat.id)
        if not user_id in translations.UL:
            translations.UL.update({user_id: 0})
            add_user(message.chat.id, '@' + message.from_user.username, 0)
        bot.send_message(message.chat.id, translations.MT[0][translations.UL[user_id]])

        helpp(message)
    except:
        print ('\x1b[0;30;41m' + "Error in start() !" + '\x1b[0m')


@bot.message_handler(content_types=['text'])
def snm(message):
    try:
        if message.chat.id in STATES:
            user_lang = translations.UL[str(message.chat.id)]
            bot.send_message(message.chat.id, translations.MT[3][user_lang])

            songs = search_track_by_name(message.text)
            user_id = str(message.chat.id)

            user_songs = {}

            for song in songs:  # creating a list of songs with all necessary data
                unique_song_link = song.link[song.link.rindex('/') + 1:]
                user_songs.update({unique_song_link: [song.artist.name + ' - ' + song.title, song.link, song.title, song.artist.name, song.album.title]})

            if len(songs) > 0:
                markup = telebot.types.InlineKeyboardMarkup()
                for i in range(len(songs)):
                    unique_song_id = songs[i].id

                    markup.add(telebot.types.InlineKeyboardButton(songs[i].artist.name + ' - ' + songs[i].title,
                                                                  callback_data='S' + str(unique_song_id)))

                bot.send_message(message.chat.id, translations.MT[4][user_lang], reply_markup=markup)

            else:
                bot.send_message(message.chat.id, translations.MT[5][user_lang])

            STATES.remove(message.chat.id)

        else:
            helpp(message)
    except:
        print ('\x1b[0;30;41m' + "Error in snm() !" + '\x1b[0m')


@bot.message_handler(func=lambda message: True)
def other(message):
    helpp(message)


bot.polling()
