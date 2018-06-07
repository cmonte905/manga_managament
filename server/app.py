import flask_wms
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    """
    #TODO: Get rid of this endpoint soon, it is just a sanity check
    """
    return 'Hello world, this should not be open to the internet'

@app.route('/manga/create', methods=['POST'])
def post_create():
    """
    Create endpoint, writes to the database user's new entry
    """
    req_data = request.get_json()

    print('This is the request itself \n', req_data)
    name = req_data['name']
    chapter = req_data['chapter']
    site = req_data['site']
    print('\nThe function that is selected: {0} {1} {2}\n'.format(name, chapter, site))
    flask_wms.write_new_data(name, chapter, site, "False")
    return 'Request recieved, create method'

@app.route('/manga/delete', methods=['POST'])
def post_delete():
    """
    #TODO Implement, user should be able to delete entries based on manga names
    """
    req_data = request.get_json()
    print('This is the request itself \n', req_data)
    print(req_data['name'])
    flask_wms.delete_entry(req_data['name'])
    return 'Request recieved, delete method'

@app.route('/manga/update', methods=['POST'])
def post_update():
    """
    #TODO IMPLEMENT -> Update endpoint, users can update either the chapter or if they finished reading something
    """
    req_data = request.get_json()
    function = req_data['function']
    if function == 'finish':
        flask_wms.update_finish(req_data['name'])
        print('App, finished request for manga {0}'.format(req_data['name']))
    elif function == 'chapter':
        flask_wms.update_chapter_number(req_data['name'], req_data['new_chapter'])
        print("chapter method, changes stuff")
    return 'Request recieved, update method'

@app.route('/manga/read', methods=['GET'])
def post_read():
    """
    Returns json of database content
    """
    mangos = flask_wms.read_data()  # from flask_wms
    return jsonify(mangos)

if __name__ == "__main__":
    app.run(debug=True)
