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

# Global variables for the colors to be displayed in the terminal
COLOR = Fore.GREEN #+ Back.BLACK
ERROR = Fore.RED + Back.BLACK

def get_parser():
    """
    Returns parser
    """
    parser = argparse.ArgumentParser(description='Help keep mangas order organized,' +
                                     'some of these aruments might not be implemented')
    parser.add_argument('-n', '--new',
                        help='Goes through a prompt for new entry', action='store_true')
    parser.add_argument('-u', '--update',
                        help='Propts user to update a manga entry from a list', action='store_true')
    parser.add_argument('-l', '--list',
                        help='Lists all mangas that are stored', action='store_true')
    parser.add_argument('-d', '--delete',
                        help='Delete entries in using a prompt', action='store_true')
    parser.add_argument('-f', '--finished',
                        help='Set a manga to finished', action='store_true')
    return parser.parse_args()

def read_data(print_flag):
    """
    Reads in data from the database at the server,
    """
    # TODO Change the server when this gets deployed to a server
    req = requests.get('http://localhost:5000/manga/read')
    mangos = []
    for i in req.json():
        mangos.append(manga(i[0], i[1], i[2], i[3]))
    if print_flag:
        for i in mangos:
            print(i)
    return mangos

def delete_entry():
    """
    Deletes an entry from a list, might make a finish flag to remember what it
    is that i have read
    """
    m_list = read_data()
    for i in req.json():
        mangos.append(manga(i[0], i[1], i[2], i[3]))

    for counter, value in enumerate(m_list):
        print('{0}: {1}'.format(counter, value))
    delete_chapter_number = int(input(  # PEP8 bullshit
        COLOR + 'Enter the number of the chapter you want to delete from the data\n'))
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
        req = requests.post('http://localhost:5000/manga/create', json=manga_data)
        print(req.text)
    else:
        print(COLOR + 'That entry is already in the list, use update instead')

def update_propmt():
    """
    Prompts user to update a manga given
    """
    m_list = read_data(True)
    update_chapter_number = int(input(COLOR + 'Enter the number of the chapter you want to update\n'))

    if m_list[update_chapter_number]:
        print(COLOR + 'The index is correct')
    else:
        print(ERROR + 'The index is wrong')
    # Gives the option to update either the name and/or the website it gets read from
    chapter_update_flag = input(COLOR + 'Would you like to update the current chapter? y/N?\n')
    if chapter_update_flag == 'y' or chapter_update_flag == 'Y':
        new_chapter = int(input(COLOR + 'Enter the new current chapter: '))
        m_list[update_chapter_number].chapter = new_chapter

    website_update_flag = input( # PEP8 on its bullshit
        COLOR + 'Would you like to update the website associated with that entry? y/N?\n')
    if website_update_flag == 'Y' or website_update_flag == 'y':
        new_site = input(COLOR + 'Please enter the new site: ')
        m_list[update_chapter_number].website = new_site

    write_data(m_list)

def main():
    """ Main Function
    In the future, Put this on a databse, if local, then sqlite, otherwise, maybe some nosql thing
    Then on the web
    """
    args = get_parser()
    if args.new:  # Prompts user to create new entry to store
        new_prompt()
    elif args.update:  # Prompts the user to update either the chapter number or finish flag
        update_propmt()
    elif args.list:  # Prints out data from database on the console
        read_data(True)
    elif args.delete:  # Prompts user to delete an entry from the database
        delete_entry()
    # Probably not going to use this, just have the one function do it instead
    elif args.finished:
        update_finish()

if __name__ == '__main__':
    main()
