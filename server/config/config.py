# Importing config
import os
import pathlib
from server.constants import CollectionNames


class BaseConfig(object):

    # DEBUGGING
    DEBUG = False

    # PATH
    BASE_PATH = '/'
    APP_PATH = '/mnt/ext/opt/boxafe'
    STORAGE_PATH = os.environ.get('STORAGE_PATH', APP_PATH)
    LOGS_PATH = APP_PATH + '/logs'

    # CONFIG FILES
    CONF_PATH_ULINUX = '/etc/config/uLinux.conf'
    CONF_PATH_SMB = '/etc/config/smb.conf'
    # PYTHON_PATH = APP_PATH + '/packages/python/bin/python3'

    # SERVER INFO
    SERVER_PROTOCOL = 'http'
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = '9046'

    # MONGO DB INFO
    MONGO_PROTOCOL = 'mongodb'
    MONGO_IP = '127.0.0.1'
    MONGO_PORT = '9045'
    MONGO_DB_NAME = 'boxafe'
    MONGO_URI = ''

    def __init__(self):
        self.set_mongo_uri()

    def set_mongo_uri(self):
        self.MONGO_URI = self.MONGO_PROTOCOL + '://' + self.MONGO_IP + \
            ':' + self.MONGO_PORT + '/' + self.MONGO_DB_NAME


class DevelopmentConfig(BaseConfig):

    # DEBUGGING
    DEBUG = True

    # SERVER INFO
    SERVER_IP = '0.0.0.0'
    SERVER_PORT = '9046'

    # MONGO DB INFO
    MONGO_IP = "172.17.30.46"
    MONGO_PORT = '9045'
    PYTHON_PATH = 'python'

    BASE_PATH = str(pathlib.Path(__file__).parent.parent.absolute())
    STORAGE_PATH = BASE_PATH + '/storage'
    LOGS_PATH = BASE_PATH + '/logs'

    def __init__(self):
        super(DevelopmentConfig, self).__init__()


class ProductionConfig(BaseConfig):

    def __init__(self):
        super(ProductionConfig, self).__init__()


def load_config(env=None):
    try:
        env = os.environ.get('FLASK_ENV')
        if env:
            env = env.lower()

        if env == 'dev' or env == 'development':
            return DevelopmentConfig()
        elif env == 'prod' or env == 'production':
            return ProductionConfig()
        else:
            return ProductionConfig()
    except Exception as err:
        print(err)

    return DevelopmentConfig()
