import sqlite3

class DB:
    """
    Used to connect to a sqlite3 db
    """
    m_db_connection = None
    m_db_cursor = None

    def __init__(self):
        """
        Connects to the db
        :param db: Database to connect too
        """
        self.m_db_connection = sqlite3.connect('manga.db')
        self.m_db_cursor = self.m_db_connection.cursor()

    def create_table(self):
        """
        Creates table if there is none already created
        """
        return self.m_db_cursor.execute('''CREATE TABLE IF NOT EXIST mangas (
        name TEXT, chapter TEXT, site TEXT, finished TEXT)''')

    def add_new_entry(self, n, c, s, f):
        """
        Parameters come from request
        """
        pass

    def close_connection(self):
        """
        Closes the connection to the database when done
        """
        self.m_db_connection.commit()
        self.m_db_connection.close()


#class DB:
#    """
#    Used to connect to a sqlite3 db
#    """
#
#    # Connects to a test db, then creates a test table
#    conn = sqlite3.connect('test.db')
#    c = conn.cursor()
#
#    #c.execute(''' Create table stocks
#    #              (date text, trans text, symbol text, qty real, price real)''')
#    c.execute(''' Create table mangas
#                  (name text, chapter text, website text, finished_flag text)''')
#
#    #c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
#    conn.commit()
#
#    conn.close()
