from flask import Flask, Response
from flasgger import Swagger
import json
from server.config.config import load_config
from server.helpers.helper import JSONEncoder
from server.swagger.templates.template import template

def create_app():
    # create flask app
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')

    # load app config
    app.config.from_object(load_config(app.env))

    # JSON encoder
    app.json_encoder = JSONEncoder

    # Setup Swagger
    swagger_config = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'specifications',
                "route": '/specifications.json',
                "rule_filter": lambda rule: True,  
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/level1/static",
        "specs_route": "/apidocs/"
    }

    # register api documentation
    Swagger(
        app,
        template=template(
            app.config.get('SERVER_IP'),
            app.config.get('SERVER_PORT'),
            app.config.get('BASE_PATH')
        ),
        config=swagger_config
    )

    # Error handlers
    @app.errorhandler(404)
    def handle_not_found_error(error):
        return Response(
            response=json.dumps(
                {'error': {'error_code': 'not_found', 'message': str(error)}}),
            status=404,
            mimetype='application/json')

    @app.errorhandler(405)
    def handle_method_not_allowed_error(error):
        return Response(
            response=json.dumps(
                {'error': {'error_code': 'method_not_allowed', 'message': str(error)}}),
            status=405,
            mimetype='application/json')

    @app.route('/')
    def index():
        return 'ADVANCED API SERVER !!!'

    return app
