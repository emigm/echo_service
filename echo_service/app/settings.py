'''Application settings'''
import os

# Application settings
APP_NAME = 'ECHO_SERVICE'
APP_ERR_CODE_PREFIX = APP_NAME
APP_UUID_LENGTH = 32  # Bytes

HTTP_PROXY = os.environ.get('APP_HTTP_PROXY')
HTTPS_PROXY = os.environ.get('APP_HTTPS_PROXY')
NO_PROXY = os.environ.get('APP_NO_PROXY')

# Logger settings
LOGGER_LEVEL = os.environ['APP_LOGGER_LEVEL']
LOGGER_PATH = os.environ['APP_LOGGER_PATH']
LOGGER_CONFIG = {
    'version': 1,
    'formatters': {
        'json_basic': {
            'format': ('{"timestamp" : "%(asctime)s", '
                       '"level" : "%(levelname)s", "message" : "%(message)s"}'),
            'datefmt': None,
        },
        'json_verbose': {
            'format': ('{"timestamp" : "%(asctime)s", "trxId" : "%(trxId)s", '
                       '"level" : "%(levelname)s", '
                       '"pathname" : "%(pathname)s", "module" : "%(module)s",'
                       '"lineno" : "%(lineno)d", "message" : "%(message)s"}'),
            'datefmt': None,
        },
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
            'formatter': 'json_basic',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(
                LOGGER_PATH, '{srv}.log'.format(srv=APP_NAME)),
            'level': LOGGER_LEVEL,
            'formatter': 'json_verbose',
            'maxBytes': 104857600,
            'backupCount': 10,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
    },
    'root': {
        'level': LOGGER_LEVEL,
        'handlers': ['stdout', 'file', ],
    },
}
