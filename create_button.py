import telebot
from downloader import search_track_by_name


def create_button_with_songs(song_name):
    tracks = search_track_by_name(song_name)

    mesage = ''


    return mesage