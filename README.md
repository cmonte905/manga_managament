# Weebo Management System
### Less useful version of myanimelist, but for manga, and only for me


#### Console Python app to help keep track of mangas using a Flask backend with sqlite3

##### Why something like this?

I did not want to start using something along the lines of myanimelist, so instead i made this.
There is nothing wrong with that site, I just like living inside the terminal and a python program would be a lot for me.
Having a terminal window open at all times is quicker to just run this in the terminal.
It is not for everyone, there is some set up required to make something like this to work.
Instructions for getting this to work will be posted later when I can be bothered to write them out



~~~
usage: flask_client.py [-h] [-n] [-u] [-l] [-d] [-f]

Help keep mangas order organized, in the cloud

outility ptional arguments:
  -h, --help      show this help message and exit
  -n, --new       Goes through a prompt for new entry
  -u, --update    Propts user to update a manga entry from a list
  -l, --list      Lists all mangas that are stored
  -d, --delete    Delete entries in using a prompt
  -f, --finished  Set an entry to finished
~~~


#### TODO

1. ~~Finish the client program, more or less the first iterations of what was created but would talk to a server instead of data being stored in a local directory~~
2. Actually write tests like I told myself I was going to
3. Get the project running on a non dev server(Looking into gunicorn with an nginx reverse proxy for that)
4. Add a new entry to the table to show what machine things are getting read on, for
    1. For example: archie -> arch box, mac -> macbook
