from os import path
#import argparse
from manga import manga
import sqlite3

"""
Weebo Management System(wms) For Flask
Mostly functions meant to be used when running on a flask backend
All functions are used to communicate with a sqlite3 db and CRUD
"""

#conn = sqlite3.connect('manga.db')
#c = conn.cursor()

def write_new_data(m_list, name, chapter, site, finish_flag):
    """
    @TODO Make this function write to a database instead
    Writes to a database, only new entries will get written
    """

    with open('data.bin', 'wb') as data_file:
        dump(m_list, data_file)

def read_data(print_data=False):
    """
    @TODO Read back data from sqlite, returns back a json object, or something parseable
    Reads in data from the data.bin file, it will return back empty list if file is empty
    """
    mangos = []
    # Some logic for if the data file is empty
    if path.isfile('data.bin'):
        with open('data.bin', 'rb') as read_file:
            mangos = load(read_file)
        if print_data:  # Wanted to avoid having another for loop here but not possible?
            for counter, value in enumerate(mangos):
                print('{0}: {1} {2}'.format(counter, value, value.website))
        return mangos
    return mangos


"""
@TODO probably not going to use this function
"""
def list_file():
    """ Prints out the data file's data """
    m_list = read_data()
    if m_list:
        for counter, value in enumerate(m_list):
            print('{0}: {1}'.format(counter, value))
    else:
        print('There are no entries saved at the moment')

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

def update_finish():
    """
    Given a list of manga, user chooses which one is now finished
    """
    m_list = read_data(True)
    if m_list:
        update_chapter_number = int(input(
            'Enter the number of the chapter you want to mark as finished\n'))
        m_list[update_chapter_number].finished = True
        write_data(m_list)

    else:
        print('Data file is empty')

