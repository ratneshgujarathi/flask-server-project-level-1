import importlib
from flask import Flask
import sys
from os import path
import os
import logging
from pathlib import Path
from server.applications import register_apis
from server.services.server import create_app

BASE_DIR = path.dirname(path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)


def import_parents(level=1):
    global __package__
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[level]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError:  # already removed
        print('error')

    __package__ = '.'.join(parent.parts[len(top.parts):])
    importlib.import_module(__package__)  # won't be needed after that


import_parents()

# Create flask App
app = create_app()
app.config['SECRET_KEY'] = 'B0KS@PH2OI9'

# register apis - should be the last
register_apis(app)


@app.after_request
def apply_caching(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9046, debug=False, use_reloader=False)
