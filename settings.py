
from environs import Env
env = Env()
env.read_env()

PATH = "data"
GROUPS_ID = env.list("GROUP_ID")
GROUPS_NAMES = env.list("GROUP_NAMES")

for i in range(len(GROUPS_ID)): # str -> int
    GROUPS_ID[i] = int(GROUPS_ID[i])

TOKEN = env.str('TOKEN')
DATABASE_PATH = env.str('DATABASE_PATH')

DEEZER_SONG_PRELINK = 'https://www.deezer.com/track/'

ADMINS = env.list("ADMINS")
ADMINS_DESTINATION = {}


for admin in ADMINS:
    ADMINS_DESTINATION.update({str(admin): 0}) # admin_id : channel to send

for i in range(len(ADMINS)):
    ADMINS[i] = int(ADMINS[i])

GROUPS_ID_NAMES = {} # target dict
for i in range(len(GROUPS_ID)):
    GROUPS_ID_NAMES.update({str(GROUPS_ID[i]):GROUPS_NAMES[i]})

