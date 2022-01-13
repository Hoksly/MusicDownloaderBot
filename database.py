import sqlite3
from settings import DATABASE_PATH
from translations import UL

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

    cur.execute("""CREATE TABLE IF NOT EXISTS User(
                ID INT PRIMARY KEY,
                LANGUAGE INT,
                LINK TEXT,
                COUNTER INT)
    """)

    con.commit()


def find_track(name, album, artist):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    cur.execute("""
    SELECT Telegram_id FROM Track WHERE Name = ? AND Artist = ? AND Album = ?
    """, (name, artist, album))

    return cur.fetchone()


def add_track(track_id, name, artist, album, file_id):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    cur.execute(
        """
        INSERT INTO Track (ID, Name, Artist, Album, Telegram_id) VALUES (?, ?, ?, ?, ?)
        """, (track_id, name, artist, album, file_id)
    )
    con.commit()


def add_user(user_id, user_link='@none', lang=0):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute("SELECT LINK FROM User WHERE ID = ?", (user_id,))
    if not cur.fetchone():
        cur.execute("INSERT INTO User(ID, LANGUAGE, LINK, COUNTER) VALUES (?, ?, ?, ?)", (user_id, lang, user_link, 0))
    con.commit()


def update_user_language(user_id, new_lang):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute('SELECT COUNTER FROM User WHERE ID = ?', (user_id,))
    l = cur.fetchone()

    if l:
        cur.execute("""UPDATE User SET LANGUAGE = ? WHERE ID = ?""", (new_lang, user_id))

    else:
        add_user(user_id, '@none', new_lang)

    con.commit()


def update_user_song_counter(user_id):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute('SELECT COUNTER FROM User WHERE ID = ?', (user_id,))
    if cur.fetchone():
        cur.execute("""UPDATE User SET COUNTER = COUNTER + 1 WHERE ID = ?""", (user_id,))
    else:
        add_user(user_id, '@none', 0)
    con.commit()


def load_users_languages():
    con = sqlite3.connect(DATABASE_PATH)

    cur = con.cursor()

    cur.execute("""
    SELECT ID, LANGUAGE FROM User
    """)

    users = cur.fetchall()
    for el in users:
        UL.update({str(el[0]): int(el[1])})


if __name__ == '__main__':
    recreate_db()
    load_users_languages()