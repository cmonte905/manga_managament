from pickle import load, dump
from os import path
import argparse
from manga import manga
#import request  # Might make a client to manage these things on a server


"""
Weebo Management system(wms)
Console based program designed to make managing manga a bit easier.
It uses command line arguments to get information
"""

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
    # Might not use these things anymore
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
    return parser.parse_args()

def write_data(m_list):
    """
    Writes list to a data file and nothing else
    """
    with open('data.bin', 'wb') as data_file:
        dump(m_list, data_file)

def read_data(print_data=False):
    """
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

def list_file():
    """ Prints out the data file's data """
    m_list = read_data()
    if m_list:
        for counter, value in enumerate(m_list):
            print('{0}: {1} {2}'.format(counter, value, value.website))
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


def update_chapter(name, new_chapter):
    """
    @ TODO - Figure out if this function is still needed
    Updates current chapter given a name
    """
    mangos = read_data()
    for i in mangos:
        print(i)

def update_finish():
    m_list = read_data(True)


def new_prompt():
    """
    Makes a new manga object then stores it into the list to be stored in a data file
    """
    m_list = read_data()
    new_manga_name = input('Enter name name of the manga to add\n')
    in_list_check = False
    for i in m_list:
        if new_manga_name == i.name:
            in_list_check = True
            break
    if not in_list_check:
        new_manga_chapter = input('Enter the current chapter of said manga\n')
        new_manga_site = input('enter the site that it is getting read on\n')
        new_manga = manga(new_manga_name, new_manga_chapter, new_manga_site)
        print(new_manga)
        m_list.append(new_manga)
        write_data(m_list)
    else:
        print('That entry is already in the list, use update instead')

def update_propmt():
    """
    Prompts user to update a manga given
    """
    m_list = read_data(True)
    update_chapter_number = int(input('Enter the number of the chapter you want to update\n'))

    # Gives the option to update either the name and/or the website it gets read from
    chapter_update_flag = input('Would you like to update the current chapter? y/N?\n')
    if chapter_update_flag == 'y' or chapter_update_flag == 'Y':
        new_chapter = int(input('Enter the new current chapter'))
        m_list[update_chapter_number].chapter = new_chapter

    website_update_flag = input( # PEP8 on its bullshit
        'Would you like to update the website associated with that entry? y/N?\n')
    if website_update_flag == 'Y' or website_update_flag == 'y':
        new_site = input('Please enter the new site\n')
        m_list[update_chapter_number].website = new_site

    write_data(m_list)

def main():
    """ Main Function
    In the future, Put this on a databse, if local, then sqlite, otherwise, maybe some nosql thing
    Then on the web
    """
    args = get_parser()
    # Prefer it if these two things did not overlap
    #print(args)
    if args.new:
        new_prompt()
    elif args.update:
        update_propmt()
    elif args.list:
        list_file()
    elif args.delete:
        delete_entry()
    elif args.finished:
        update_finish()

if __name__ == '__main__':
    main()
