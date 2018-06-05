from os import path
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
    Reads in data from the data.bin file, it will return back empty list if file is empty
    """
    mangos = database.read_data()
    return mangos


def delete_entry():
    """
    Deletes an entry from a list, might make a finish flag to remember what it
    is that i have read
    """
    m_list = read_data()
    for counter, value in enumerate(m_list):
        print('{0}: {1}'.format(counter, value))
    delete_chapter_number = int(input(  # PEP8 bullshit
        'Enter the number of the chapter you want to delete from the data\n'))
    m_list.pop(delete_chapter_number)
    write_data(m_list)

def update_chapter_number(new_chapter):
    pass

def update_finish():
    """
    Given a list of manga, user chooses which one is now finished
    """
    m_list = read_data(True)
    if m_list:
        update_chapter_number = int(input(
            'Enter the number of the chapter you want to mark as finished\n'))
    else:
        print('There are no entries in the database empty')
