import sqlite3

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

    con.commit()


def find_track(name, album, artist):
    con = sqlite3.connect('data/main.sqlite3')
    cur = con.cursor()
    print()

    cur.execute("""
    SELECT Telegram_id FROM Track WHERE Name = ? AND Artist = ? AND Album = ?
    """, (name, artist, album))


    return cur.fetchone()


def add_track(name, artist, album, file_id):
    con = sqlite3.connect('data/main.sqlite3')
    cur = con.cursor()

    cur.execute(
        """
        INSERT INTO Track (Name, Artist, Album, Telegram_id) VALUES (?, ?, ?, ?)
        """, (name, artist, album, file_id)
    )
    con.commit()


find_track('Name', 'Album', 'Artist')
