import sqlite3

class DB:
    """
    Used to connect to a sqlite3 db
    Most CRUD operations should be done here, such as create, delete, read
    """
    m_db_connection = None
    m_db_cursor = None

    def __init__(self):
        """
        Connects to the manga database
        :param db: Database to connect too
        """
        self.m_db_connection = sqlite3.connect('manga.db')
        self.m_db_cursor = self.m_db_connection.cursor()

    def create_table(self):
        """
        Creates table if there is none already created
        """
        return self.m_db_cursor.execute('''CREATE TABLE IF NOT EXISTS mangas (
        name TEXT, chapter TEXT, site TEXT, finished TEXT)''')

    def add_new_entry(self, name, chapter, site, finish):
        """
        Parameters come from request
        :param name -> name of manga
        :param chapter -> current chapter
        :param site -> website it is getting read on
        :param finish -> finish flag
        """
        return self.m_db_cursor.execute('INSERT INTO mangas VALUES (?, ?, ?, ?)',
                                        (name, chapter, site, finish))

    def delete_entry(self, name):
        """
        Deletes entries by name
        :param n -> name of manga to delete
        """
        return self.m_db_cursor.execute('DELETE FROM mangas WHERE name = (?)', (name))

    def read_data(self):
        """
        Reads/returns all data from the database
        """
        return self.m_db_cursor.execute('Select * from mangas')

    def close_connection(self):
        """
        Closes the connection to the database when done
        """
        self.m_db_connection.commit()
        self.m_db_connection.close()

#    #c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
