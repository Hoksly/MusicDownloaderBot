import subprocess
import deezer_cp
from settings import PATH


def download_track(url, folder=PATH, name= None, artist= None, album = None):
    subprocess.run("python3 -m deemix {} -p {}".format(url, folder), shell=True)
    return name, artist, album


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

