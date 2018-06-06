from db import DB

"""
Weebo Management System(wms) For Flask
Mostly functions meant to be used when running on a flask backend
All functions are used to communicate with a sqlite3 db and CRUD
For the updates, only chapter, website and finish flag can be changed
"""

database = DB()
def write_new_data(name, chapter, site, finish):
    """
    @TODO Make this function write to a database instead
    Writes to a database, only new entries will get written
    """
    print('From wms:', name, chapter, site, finish)
    database.add_new_entry(name, chapter, site, finish)

def read_data():
    """
    @TODO Read back data from sqlite, returns back a json object, or something parseable
    """
    mangos = database.read_data()
    return mangos

def delete_entry(manga_name):
    """
    Deletes an entry from a list, might make a finish flag to remember what it
    is that i have read
    """
    print('from flask wms: ', manga_name)
    database.delete_entry(manga_name)

def update_chapter_number(name, new_chapter):
    """
    Questioning if this is necessary, to have this helper function, though more
    there could be some kind of validation done here before being sent off to
    be recorded
    """
    database.update_chapter(name, new_chapter)
    database.commit_db()

def update_finish(name):
    """
    Given a list of manga, user chooses which one is now finished
    """
    database.update_finish(name)
    database.commit_db()
