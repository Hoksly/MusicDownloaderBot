
from environs import Env
env = Env()
env.read_env()

PATH = "data"
GROUP_ID = env.int("GROUP_ID")
TOKEN = env.str('TOKEN')
DATABASE_PATH = env.str('DATABASE_PATH')

DEEZER_SONG_PRELINK = 'https://www.deezer.com/track/'

