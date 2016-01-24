

import logging


class LoggingMixin(object):
    def log(self):
        try:
            return self.logger
        finally:
            self.logger = get_app_logger()
            return self.logger


def get_app_logger():
    return logging.getLogger('tornado.application')
