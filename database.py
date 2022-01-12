import sqlite3
from settings import DATABASE_PATH
def recreate_db():
    con = sqlite3.connect('data/main.sqlite3')
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Track (
                ID INT PRIMARY KEY,
                Name TEXT, 
                Artist TEXT, 
                Album TEXT , 
                Telegram_id TEXT 
                
                )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS User
                ID INT PRIMARY KEY,
                LANGUAGE INT,
                LINK TEXT,
                COUNTER INT
    """)

    con.commit()


def find_track(name, album, artist):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    cur.execute("""
    SELECT Telegram_id FROM Track WHERE Name = ? AND Artist = ? AND Album = ?
    """, (name, artist, album))

    return cur.fetchone()


def add_track(name, artist, album, file_id):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    cur.execute(
        """
        INSERT INTO Track (Name, Artist, Album, Telegram_id) VALUES (?, ?, ?, ?)
        """, (name, artist, album, file_id)
    )
    con.commit()


def add_user(user_id, user_link = '@none', lang = 0 ):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    cur.execute("INSERT INTO User(ID, LANGUAGE, LINK, COUNTER) VALUES (?, ?, ?, ?)", (user_id, lang, user_link, 0))
    con.commit()


def update_user_language(user_id, new_lang):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    cur.execute("""UPDATE User SET LANGUAGE = ? WHERE ID = ?""", (new_lang, user_id))

    con.commit()

def update_user_song_counter(user_id, value = 1):
    pass