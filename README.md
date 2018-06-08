# Weebo Management System
### Less useful version of myanimelist, but for manga, and only for me

usage: flask_client.py [-h] [-n] [-u] [-l] [-d] [-f]

Help keep mangas order organized, in the cloud

optional arguments:
  -h, --help      show this help message and exit
  -n, --new       Goes through a prompt for new entry
  -u, --update    Propts user to update a manga entry from a list
  -l, --list      Lists all mangas that are stored
  -d, --delete    Delete entries in using a prompt
  -f, --finished  Set an entry to finished



#### TODO

1. ~~Finish the client program, more or less the first iterations of what was created but would talk to a server instead of data being stored in a local directory~~
2. Actually write tests like I told myself I was going to
2. Get the project running on a non dev server(Looking into gunicorn with an nginx reverse proxy for that)
3. Add a new entry to the table to show what machine things are getting read on, for
  1. For example: archie -> arch box, mac -> macbook


