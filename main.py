import subprocess
import os
import telebot
import settings
import translations
from downloader import download_track, search_track_by_name
from database import find_track, add_track


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
    # extract user id from call.data
    ind = call.data.index ('|')
    user = call.data [1: ind]
    cursel = int (call.data [ind + 1:])

    if call.data [0] == 'S':
        download_and_send (SONGS [user][cursel][1], call.message.chat.id, SONGS [user][cursel][0], call.message.id,
                          SONGS [user][cursel][2], SONGS [user][cursel][3], SONGS [user][cursel][4])
        SONGS.pop (str (user))  # chat_id = message.chat.id
    elif call.data [0] == 'L':
        translations.UL.update ({user: cursel})
        # notificate


@bot.message_handler (content_types=['text'])
def g1g (message):
    global STATES
    global SONGS
    if message.chat.id in STATES:
        bot.send_message (message.chat.id, "Searching...")
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
                markup.add (telebot.types.InlineKeyboardButton (songs[i].artist.name + ' - ' + songs [i].title, callback_data = 'S' + str (message.chat.id) + "|" + str (i)))
            bot.send_message (message.chat.id, "Songs:", reply_markup=markup)

            STATES.remove (message.chat.id)

        else:
            bot.send_message (message.chat.id, "Sorry, couldn't find any songs with this name. Please try again")
    else:
        helpp (message)


@bot.message_handler (commands=['lang'])
def lang (message):
    markup = telebot.types.InlineKeyboardMarkup ()
    for i in range (len (translations.LGS)):
        markup.add (telebot.types.InlineKeyboardButton (translations.LGS [i], callback_data = 'L' + str (message.chat.id) + "|" + str (i)))
    bot.send_message (message.chat.id, "Choose your language:", reply_markup=markup)

    
@bot.message_handler (commands=['search'])
def search (message):
    global STATES
    user_lang = translations.UL [str (message.chat.id)]
    bot.send_message (message.chat.id, translations.MT [2] [user_lang])
    STATES.add (message.chat.id)


@bot.message_handler (commands=['help'])
def helpp (message):
    try:
        user_lang = translations.UL [str (message.chat.id)]
    except KeyError:
        user_lang = 0
        translations.UL.update({str(message.chat.id): 0})
    bot.send_message (message.chat.id, translations.MT [0] [user_lang])


@bot.message_handler (commands=['start'])
def start (message):
    user_id = str (message.chat.id)
    if not user_id in translations.UL: # ?
        translations.UL.update ({user_id: 0})
    bot.send_message (message.chat.id, translations.MT [1] [translations.UL [user_id]])
    helpp ()

    
@bot.message_handler (func=lambda message: True)
def other (message):
    helpp (message)


bot.polling ()
