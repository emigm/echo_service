'''Application definitions and URL mappings'''
import logging
import logging.config
import tornado.web

import echo_service.service.handlers.echo as echo
import echo_service.app.settings as settings


LOGGER = logging.getLogger()
logging.config.dictConfig(settings.LOGGER_CONFIG)


BACKEND = tornado.web.Application(
    [
        (r'.*/echo/?$', echo.EchoHandler),
    ], logger=LOGGER)
