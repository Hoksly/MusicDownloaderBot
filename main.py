import subprocess
import os
import telebot
import settings
import translations
from downloader import download_track, search_track_by_name
from database import find_track, add_track
import time

bot = telebot.TeleBot (settings.TOKEN)


STATES = set ()  # set: id
SONGS = {}  # dictionary: id - list [songs]

def download_and_send (url, chat_id, file_name, message_id, song_name, artist, album):
    track_id = find_track(name=song_name, album=album, artist=artist)

    if track_id:
        bot.send_audio (chat_id, track_id [0])
        return

    download_track (url)
    if os.path.exists ('data/' + file_name + '.mp3'):
        bot.send_audio (chat_id, open('data/' + file_name + '.mp3', 'rb'))
        time.sleep(1)
        msg = bot.forward_message (settings.GROUP_ID, chat_id, message_id + 1)
        file_id = msg.audio.file_id

        if file_id:
            add_track(song_name, artist, album, file_id)

        os.remove('data/' + file_name + '.mp3')

    else:
        bot.send_message (chat_id, "Something went wrong. Please, try again. If this message persists, contact with @hoksly")

    # clearing user data


@bot.callback_query_handler (func=lambda call: True)
def call_handler (call):
    cursel = int (call.data [1:])
    user = str (call.message.chat.id)
    if call.data [0] == 'S':
        download_and_send (SONGS [user][cursel][1], call.message.chat.id, SONGS [user][cursel][0], call.message.id,
                          SONGS [user][cursel][2], SONGS [user][cursel][3], SONGS [user][cursel][4])
        SONGS.pop (str (user))  # chat_id = message.chat.id
    elif call.data [0] == 'L':
        translations.UL.update ({user: cursel})
        bot.send_message (call.message.chat.id, translationsCL [cursel])

@bot.message_handler (commands=['lang'])
def lang (message):
    #if message.chat.id in STATES:
    user_lang = translations.UL [str (message.chat.id)]
    markup = telebot.types.InlineKeyboardMarkup ()
    for i in range (len (translations.LGS)):
        markup.add (telebot.types.InlineKeyboardButton (translations.LGS [i], callback_data = 'L' + str (i)))
    bot.send_message (message.chat.id, translations.MT [6] [user_lang], reply_markup=markup)

    
@bot.message_handler (commands=['search'])
def search (message):
    #if message.chat.id in STATES:
    global STATES
    try:
        user_lang = translations.UL [str (message.chat.id)]
    except KeyError:
        user_lang = 0
        translations.UL.update({str(message.chat.id): 0})

    bot.send_message (message.chat.id, translations.MT [2] [user_lang])
    STATES.add (message.chat.id)


@bot.message_handler (commands=['help'])
def helpp (message):
    #if message.chat.id in STATES:
    try: # думаю, лучше всё же убрать, но после того, как реализум загрузку UL с файла
        user_lang = translations.UL [str (message.chat.id)]
    except KeyError:
        user_lang = 0
        translations.UL.update ({str (message.chat.id): 0})
    bot.send_message (message.chat.id, translations.MT [1] [user_lang])


@bot.message_handler (commands=['start'])
def start (message):
    #if message.chat.id in STATES:
    user_id = str (message.chat.id)
    if not user_id in translations.UL:
        translations.UL.update ({user_id: 0})
    bot.send_message (message.chat.id, translations.MT [0] [translations.UL [user_id]])
    helpp (message)

@bot.message_handler (content_types=['text'])
def g1g (message):
    global STATES
    if message.chat.id in STATES:
        user_lang = translations.UL [str (message.chat.id)]
        bot.send_message (message.chat.id, translations.MT [3] [user_lang])
        global SONGS
        songs = search_track_by_name (message.text)
        user_id = str (message.chat.id)
        SONGS.update ({user_id: []})
        user_songs = []
        for song in songs:  # creating a list of songs with all necessary data
            user_songs.append ([song.artist.name + ' - ' + song.title, song.link, song.title, song.artist.name, song.album.title])

        SONGS.update ({user_id: user_songs})  # updating of global dict ()

        if len (songs) > 0:
            markup = telebot.types.InlineKeyboardMarkup ()
            for i in range (len (songs)):
                markup.add (telebot.types.InlineKeyboardButton (songs[i].artist.name + ' - ' + songs [i].title, callback_data = 'S' + str (i)))
            bot.send_message (message.chat.id, translations.MT [4] [user_lang], reply_markup=markup)

            STATES.remove (message.chat.id)

        else:
            bot.send_message (message.chat.id, translations.MT [5] [user_lang])
    else:
        helpp (message)

    
@bot.message_handler (func=lambda message: True)
def other (message):
    helpp (message)


bot.polling ()
