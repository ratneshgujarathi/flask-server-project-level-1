from flask import Blueprint
core_v1 = Blueprint('api_core_v1', __name__, url_prefix='/v1/core')
from server.app import db
from server.constants import CollectionNames

@core_v1.route('/db/<entry>', methods=['GET'])
def db_entry(entry):
    db[CollectionNames.EVENT_LOGS].insert_one({'name': entry})
    return 'success'
