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
    return parser.parse_args()

def write_data(name, chapter, site):
    """
    Function will write data if there is no data file, if there is a file detected,
    then it will get read instead
    """
    mangos = read_data() # Holds  mangas in an array for reading and writing
    print(mangos)
    manga_entry = manga(name, chapter, site)
    print(manga_entry)

def read_data():
    """
    Reads in data from the data.bin file, it will return back
    a list of objects, if there is  no fine, it will return an empty list
    """
    mangos = []
    # Some logic for if the data file is empty
    if path.isfile('data.bin'):
        print('Data.bin file exists')
        with open('data.bin', 'rb') as r:
            mangos = load(r)
        return mangos
    return mangos

def add_to_list(new_manga):
    """
    Gets the list saved in the bin file, adds new entry, then saves it again
    """
    current_list = read_data()
    current_list.append(new_manga)

def update_chapter(name, new_chapter):
    """
    Updates current chapter given a name
    """
    mangos = read_data()
    for i in mangos:
        print(i)

def main():
    """
    Main function
    First, get the fucking argument parser to work
    Update chapter, website
    New
    delete
    set complete
    In the future, Put this on a databse
    Then on the web
    """
    args = get_parser()
    print(args)
    print(args.new)
    print(args.update)

if __name__ == '__main__':
    main()
