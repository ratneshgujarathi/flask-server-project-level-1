import importlib
import logging


SERVICES = [
    # # auth module
    {'path': '.applications.core.api', 'blueprint': 'auth'},

    # Core module
    {'path': '.applications.core.api.v1', 'blueprint': 'core_v1'}
]


def register_apis(app):
    try:
        for service in SERVICES:
            module = importlib.import_module(service['path'], package='server')
            app.register_blueprint(getattr(module, service['blueprint']))
        logging.info('Registered all the APIs')
    except Exception as err:
        logging.exception(f"Failed to register APIs: {err}")
