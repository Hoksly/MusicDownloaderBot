import subprocess
import deezer_cp
from settings import PATH
from deemix.__main__ import download


def download_track(url, folder=PATH):
    download(path=folder, bitrate=None, portable=True, url=[url])


def search_track_by_name(name):
    """
    Searching track by it's name

    :param name:
    :return: list [Track]
    """
    client = deezer_cp.Client()
    trak = deezer_cp.Track

    return client.search(name, limit=15)


def search_albums(name):
    client = deezer_cp.Client()

    return client.search_albums(name)


def give_track_data(track_id:int):
    client = deezer_cp.Client()
    track = client.get_track(track_id)


    return track.title, track.artist.name, track.album.title

if __name__ == '__main__':
    client = deezer_cp.Client()

