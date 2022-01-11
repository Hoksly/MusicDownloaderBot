import subprocess
import os
import telebot
from downloader import download_track, search_track_by_name
from database import find_track, add_track
from settings import GROUP_ID
bot = telebot.TeleBot("your token")
# bot = aiogram.Bot(token= "2092930992:AAHylQNSDsf8A-jlzXcrERLxg3llmabpRXY")

STATE = "None"
SONGS = []


def mkkbd(songs):
    markup = telebot.types.InlineKeyboardMarkup()

    # for text, link in strlst.items ():

    for i in range(len(songs)):
        # markup.add (telebot.types.InlineKeyboardButton (text, link, link))
        markup.add(telebot.types.InlineKeyboardButton(songs[i].artist.name + ' - ' + songs[i].title,
                                                      callback_data=str(i)))

    # markup.add(telebot.types.InlineKeyboardButton("Download all", callback_data=len(SONGS)))

    return markup


def download_and_send(url, chat_id, file_name, message_id, song_name, artist, album):
    track_id = find_track(name=song_name, album=album, artist=artist)

    if track_id:
        bot.send_audio(chat_id, track_id[0])
        return

    download_track(url)
    if os.path.exists('data/' + file_name + '.mp3'):
        bot.send_audio(chat_id, open('data/' + file_name + '.mp3', 'rb'))
        msg = bot.forward_message(GROUP_ID, chat_id, message_id + 1)
        file_id = msg.audio.file_id

        if file_id:
            add_track(song_name, artist, album, file_id)

        os.remove('data/' + file_name + '.mp3')

    else:
        bot.send_message(chat_id,
                         'Something went wrong. Please try again. If this message persist connect with @hoksly')




@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    # bot.answer_callback_query(call.id, "Callback got this: " + call.data)
    # download_track(call.data)

    if int(call.data) == len(SONGS):
        for i in range(len(SONGS)):
            '''
            download_track(SONGS[int(call.data)][1])
            if os.path.exists('data/' + SONGS[int(call.data)][0] + '.mp3'):
                bot.send_audio(call.message.chat.id, open('data/' + SONGS[int(call.data)][0] + '.mp3', 'rb'))
                msg = bot.forward_message(-1001206103529, call.message.chat.id, call.message.id + 2)
                file_id = msg.audio.file_id

                if file_id:
                    add_track(all_data[1], all_data[2], all_data[3], file_id)

            else:
                bot.send_message(call.message.chat.id, 'Something went wrong. Please try again. If this message persist connect with @hoksly')
            '''

    else:
        download_and_send(SONGS[int(call.data)][1], call.message.chat.id, SONGS[int(call.data)][0],
                          call.message.id,
                          SONGS[int(call.data)][2], SONGS[int(call.data)][3], SONGS[int(call.data)][4])


'''
        
        download_track(SONGS[int(call.data[0])][1])
        if os.path.exists('data/' + SONGS[int(call.data)][0] + '.mp3'):
            bot.send_audio(call.message.chat.id, open('data/' + SONGS[int(call.data)][0] + '.mp3', 'rb'))

            # bot.send_message(call.message.chat.id, 'GG')
'''


@bot.message_handler(commands=['search'])
def handle_command_adminwindow(message):
    global STATE
    bot.send_message(message.chat.id, "Send me a name of song")
    STATE = "Searching_song"


@bot.message_handler(commands=['help'])
def gg(message):
    msg = """/search - search songs. Still testing"""
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['start'])
def gg2(message):
    msg = """Greetings from StolenProd community. \n/To start searching songs use /search"""
    bot.send_message(message.chat.id, msg)


@bot.message_handler(func=lambda message: True)
def g1g(message):
    global STATE
    global SONGS
    if STATE == "Searching_song":
        songs = search_track_by_name(message.text)
        SONGS = []
        for song in songs:
            SONGS.append([song.artist.name + ' - ' + song.title, song.link, song.title, song.artist.name, song.album.title])

        bot.send_message(message.chat.id, "searching...")
        if len(songs) > 0:
            msg = mkkbd(songs)
            bot.send_message(message.chat.id, "Songs:", reply_markup=msg)
            STATE = "None"
        else:
            bot.send_message(message.chat.id, 'Sorry, no songs was found')
    else:
        bot.send_message(message.chat.id, "Send me a command, or /help")


'''
@bot.message_handler(commands=['help'])
def gg(message):
    msg = """/search - search songs \n/search_album - search albums"""
    bot.send_audio(message.chat.id , open('data/Metallica - Battery.mp3', 'rb'))
    msg = bot.forward_message(-1001206103529, message.chat.id, message.id + 1)
    bot.send_message(message.chat.id, str(msg.id))
    bot.send_message(message.chat.id, str(msg.audio.file_id))
    file_id = msg.audio.file_id
'''

bot.polling()
