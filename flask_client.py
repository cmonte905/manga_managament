from os import path
import argparse
import requests
import json
from manga import manga
from colorama import Fore, Back, Style

"""
Weebo Management System(wms) Client
Console based program designed to make managing manga a bit easier.
It uses command line arguments to get information that gets sent off
to a flask backend
"""

# Global variables for the colors to be displayed in the terminal because why not
COLOR = Fore.YELLOW#+ Back.BLACK
ERROR = Fore.RED #+ Back.BLACK
SERVER = 'http://localhost:5000/manga'
# TODO Change the server when this gets deployed to a server


def get_parser():
    """
    Returns parser
    """
    parser = argparse.ArgumentParser(description='Help keep mangas order organized')
    parser.add_argument('-n', '--new',
                        help='Goes through a prompt for new entry', action='store_true')
    parser.add_argument('-u', '--update',
                        help='Propts user to update a manga entry from a list', action='store_true')
    parser.add_argument('-l', '--list',
                        help='Lists all mangas that are stored', action='store_true')
    parser.add_argument('-d', '--delete',
                        help='Delete entries in using a prompt', action='store_true')
    parser.add_argument('-f', '--finished',
                        help='Set an entry to finished', action='store_true')
    return parser.parse_args()

def read_data(print_flag):
    """
    Reads in data from the database at the server,
    """
    req = requests.get(SERVER + '/read')
    mangos = []
    for i in req.json():
        mangos.append(manga(i[0], i[1], i[2], i[3]))
    if mangos:
        if print_flag:
            for i in mangos:
                print(COLOR, i)
        return mangos
    else:
        print(ERROR + 'There is no data in the database')
        return []

def new_prompt():
    """
    Prompts user for information then saves sends it to be saved
    New entries are to have a finish flag of false
    """
    m_list = read_data(False)
    new_manga_name = input(COLOR + 'Enter name name of the manga to add\n')
    in_list_check = False
    # Making sure there are no duplicates in the database without getting an error
    for i in m_list:
        if new_manga_name == i.name:
            in_list_check = True
            break
    if not in_list_check:
        new_manga_chapter = input(COLOR + 'Enter the current chapter of said manga\n')
        new_manga_site = input(COLOR + 'Enter the site that it is getting read on\n')
        manga_data = {
            'name': new_manga_name,
            'chapter': new_manga_chapter,
            'site': new_manga_site
        }
        req = requests.post(SERVER + '/create', json=manga_data)
        print(req.text)
    else:
        print(COLOR + 'That entry is already in the list, use update instead')

def update_propmt(update_chapter):
    """
    Prompts user to update current chapter of a given entry as well as
    mark a given entry as finished
    """
    chapter_string = 'Enter the number of the manga whos chapter you want to update\n'
    finish_string = 'Enter the number of the manga you want to mark as finished\n'
    m_list = read_data(False)

    for counter, value in enumerate(m_list):
        print(COLOR + '{0}: {1}'.format(counter, value))
    update_entry = int(input(COLOR + chapter_string if update_chapter else finish_string))
    if m_list[update_entry]:
        print(COLOR + 'The index is correct')
    else:
        print(ERROR + 'The index is wrong')

    # Gives the option to update either the name and/or the website it gets read from
    if update_chapter:
        new_chapter = int(input(COLOR + 'Enter the new current chapter: '))
        print(m_list[update_entry].name, new_chapter)
        manga_data = {
            'function': 'chapter',
            'name': m_list[update_entry].name,
            'new_chapter': new_chapter
        }
        req = requests.post(SERVER + '/update', json=manga_data)
        print(req.text)
    # This is for the finish flag
    else:
        print(m_list[update_entry].name)
        manga_data = {
            'function': 'finish',
            'name': m_list[update_entry].name
        }
        req = requests.post(SERVER + '/update', json=manga_data)
        print(req.text)

def delete_entry():
    """
    Deletes an entry from a list, might make a finish flag to remember what it
    is that i have read
    """
    m_list = read_data(False)
    if m_list:
        for counter, value in enumerate(m_list):
            print(COLOR + '{0}: {1}'.format(counter, value))
        delete_chapter_number = int(input(  # PEP8 bullshit
            COLOR + 'Enter the number of the chapter you want to delete from the data\n'))
        try:
            print(m_list[delete_chapter_number])
            data = {'name': m_list[delete_chapter_number].name}
            req = requests.post(SERVER + '/delete', json=data)
            print(req.text)
        except IndexError:
            print('There is no entry for that number')

def print_ascii():
    """
    Prints some nice art because why not
    """
    print(COLOR + '''
      _      ____  _______
     | | /| / /  |/  / __/
     | |/ |/ / /|_/ /\ \\
     |__/|__/_/  /_/___/
    ''')

def main():
    """ Main Function
    In the future, Put this on a databse, if local, then sqlite, otherwise, maybe some nosql thing
    Then on the web
    """
    print_ascii()
    args = get_parser()
    if args.new:  # Prompts user to create new entry to store
        new_prompt()
    elif args.update:  # Prompts the user to update either the chapter number or finish flag
        update_propmt(True)
    elif args.list:  # Prints out data from database on the console
        read_data(True)
    elif args.delete:  # Prompts user to delete an entry from the database
        delete_entry()
    # Probably not going to use this, just have the one function do it instead
    elif args.finished:
        update_propmt(False)

if __name__ == '__main__':
    main()
