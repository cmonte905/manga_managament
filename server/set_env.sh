#!/usr/bin/env sh

export FLASK_DEBUG=1;export FLASK_APP=app.py
echo "Starting development server for WMS ...."
flask run --host=127.0.0.1
