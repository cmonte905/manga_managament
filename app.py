import flask_wms
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello world, this should not be open to the internet'

@app.route('/manga/create', methods=['POST'])
def post_create():
    req_data = request.get_json()

    print('This is the request itself \n', req_data)
    name = req_data['name']
    chapter = req_data['chapter']
    site = req_data['site']
    print('\nThe function that is selected: {0} {1} {2}\n'.format(name, chapter, site))
    return 'Request recieved, create method'

@app.route('/manga/delete', methods=['POST'])
def post_delete():
    req_data = request.get_json()
    print('This is the request itself \n', req_data)
    return 'Request recieved, delete method'

@app.route('/manga/read', methods=['GET'])
def post_read():
    mangos = flask_wms.read_data()  # from flask_wms
    return jsonify(mangos)

if __name__ == "__main__":
    app.run(debug=True)
