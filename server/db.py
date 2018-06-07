import sqlite3

class DB:
    """
    Used to connect to a sqlite3 db
    Most CRUD operations should be done here, such as create, delete, read
    """
    m_db_connection = None
    m_db_cursor = None

    def __init__(self, db='manga.db'):
        """
        Connects to the manga database
        :param db: Database to connect too
        """
        self.m_db_connection = sqlite3.connect(db)
        self.m_db_cursor = self.m_db_connection.cursor()

    def create_manga_table(self):
        """
        Creates table if there is none already created
        """
        self.m_db_cursor.execute('''CREATE TABLE IF NOT EXISTS mangas (
        name TEXT UNIQUE, chapter TEXT, site TEXT, finished TEXT)''')

    def add_new_entry(self, name, chapter, site, finish):
        """
        Parameters come from request
        :param name -> name of manga
        :param chapter -> current chapter
        :param site -> website it is getting read on
        :param finish -> finish flag
        """
        print('From API', name, chapter, site, finish)
        self.m_db_cursor.execute('INSERT or IGNORE INTO mangas VALUES (?, ?, ?, ?)',
                                 (name, chapter, site, finish))

    def update_chapter(self, name, new_chapter):
        """
        Updates a mangas current chapter
        """
        self.m_db_cursor.execute('UPDATE mangas SET chapter=? WHERE name=?', (new_chapter, name))

    def update_finish(self, name):
        """
        Updates a manga entry to finish
        """
        self.m_db_cursor.execute('UPDATE mangas SET finished=? WHERE name=?', ('True', name))

    def delete_entry(self, name):
        """
        Deletes entries by name
        :param n -> name of manga to delete
        """
        print(name)
        self.m_db_cursor.execute('DELETE FROM mangas WHERE name=?', (name,))
        self.m_db_connection.commit()

    def read_data(self):
        """
        Reads/returns all data from the database
        """
        self.m_db_cursor.execute('Select * from mangas')
        return self.m_db_cursor.fetchall()

    def commit_db(self):
        """
        Closes the connection to the database when done
        """
        self.m_db_connection.commit()

    def close_connection(self):
        """
        Closes the connection to the database when done
        """
        self.m_db_connection.commit()
        self.m_db_connection.close()
