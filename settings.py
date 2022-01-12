TOKEN = "token"
PATH = "data"
CONTACT = "@username"
GROUP_ID = 1 #your channel
'''
from environs import Env
env = Env()
env.read_env()

PATH = "data"
GROUP_ID = env.int("GROUP_ID")
TOKEN = env.str('TOKEN')


'''