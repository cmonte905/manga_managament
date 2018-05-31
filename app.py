#from wms import * 
from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello world, this should not be open to the internet'

@app.route("/other")
def other():
    return 'This is other'

@app.route('/manga', methods=['POST'])
def post_processing():
    req_data = request.get_json()
    print('This is the request itself \n', req_data)
    #language = req_data['language']
    function = req_data['function']
    print('\nThe function that is selected:{}\n'.format(function))

    #list_file()
    return 'Request recieved'


if __name__ == "__main__":
    app.run(debug=True)
