from pickle import load, dump
#from sys import argv
from os import path
import argparse
from manga import manga

"""
Console based program designed to make managing manga a bit easier.
It uses command line arguments to get information
"""

def get_parser():
    """
    Returns parser
    """
    parser = argparse.ArgumentParser(description='Help keep mangas order organized')
    parser.add_argument('-nn', '--new_chapter_name', dest='new_chapter_name',
                        help='Given a name, selects a manga to update its chapter')
    parser.add_argument('-nc', '--new_chapter_number', dest='new_chapter_number',
                        help='Given a name, udpates the current chapter of the manga')
    parser.add_argument('-nw', '--new_chapter_website', dest='new_chapter_website',
                        help='Given a name, udpates the site the manga is getting read on')
    # These args are to update stuff that is already in the list
    parser.add_argument('-un', '--update_chapter_name', dest='update_chapter_name',
                        help='Given a name, selects a manga to update its chapter')
    parser.add_argument('-uc', '--update_chapter_number', dest='update_chapter_number',
                        help='Given a name, udpates the current chapter of the manga')
    parser.add_argument('-uw', '--update_chapter_website', dest='update_chapter_website',
                        help='Given a name, udpates the current site the manga is getting read on')
    # Optional stuff, used for prompting, goes through a menu
    parser.add_argument('-n', '--new',
                        help='Goes through a prompt for new entry', action='store_true')
    parser.add_argument('-u', '--update',
                        help='Propts user to update a manga entry from a list', action='store_true')
    parser.add_argument('-l', '--list',
                        help='Lists all mangas that are stored', action='store_true')
    return parser.parse_args()

def write_data(m_list):
    """
    Writes list to a data file and nothing else
    """
    with open('data.bin', 'wb') as data_file:
        dump(m_list, data_file)

def read_data():
    """
    Reads in data from the data.bin file, it will return back empty list if file is empty
    """
    mangos = []
    # Some logic for if the data file is empty
    if path.isfile('data.bin'):
        print('Data.bin file exists')
        with open('data.bin', 'rb') as read_file:
            mangos = load(read_file)
        return mangos
    return mangos

def add_to_list(new_manga):
    """
    @TODO Figure out if this method should still exist
    Gets the list saved in the bin file, adds new entry, then saves it again
    """
    current_list = read_data()
    current_list.append(new_manga)

def list_file():
    m_list = read_data()
    for counter, value in enumerate(m_list):
        print('{0}: {1} {2}'.format(counter, value, value.website))

def update_chapter(name, new_chapter):
    """
    Updates current chapter given a name
    """
    mangos = read_data()
    for i in mangos:
        print(i)

def new_prompt():
    """
    Makes a new manga object then stores it into the list to be stored in a data file
    """
    new_manga_name = input('Enter name name of the manga to add\n')
    new_manga_chapter = input('Enter the current chapter of said manga\n')
    new_manga_site = input('enter the site that it is getting read on\n')
    new_manga = manga(new_manga_name, new_manga_chapter, new_manga_site)
    print(new_manga)
    m_list = read_data()
    m_list.append(new_manga)
    write_data(m_list)

def update_propmt():
    """
    Prompts user to update a manga given
    """
    m_list = read_data()
    for counter, value in enumerate(m_list):
        print('{0}: {1}'.format(counter, value))
    update_chapter_number = int(input('Enter the number of the chapter you want to update\n'))
    new_chapter = int(input('Enter the new current chapter'))
    m_list[update_chapter_number].chapter = new_chapter
    print('New current chapter')
    print(m_list[update_chapter_number].chapter)
    website_update_flag = input('Would you like to update the website associated with that entry? y/N?')
    if website_update_flag != 'N' or website_update_flag != 'N' or website_update_flag != '':
        new_site = input('Please enter the new site\n')

    write_data(m_list)

def main():
    """ Main Function
    Update chapter, website
    New
    delete
    set complete
    In the future, Put this on a databse, if local, then sqlite, otherwise, maybe some nosql thing
    Then on the web
    """
    args = get_parser()
    print(args)
    # Prefer it if these two things did not overlap
    if args.new:
        new_prompt()
    elif args.update:
        update_propmt()
    elif args.list:
        list_file()


if __name__ == '__main__':
    main()
