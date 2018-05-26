import sqlite3

class DB:
    """
    Used to connect to a sqlite3 db
    """

    # Connects to a test db, then creates a test table
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    #c.execute(''' Create table stocks
    #              (date text, trans text, symbol text, qty real, price real)''')
    c.execute(''' Create table mangas
                  (name text, chapter text, website text, finished_flag text)''')

    #c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    conn.commit()

    conn.close()
