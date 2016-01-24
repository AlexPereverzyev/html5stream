
import signal
import tornado
import tornado.ioloop
import tornado.web
import app_config

from tornado.options import options
from app_settings import settings
from logging_mixin import get_app_logger
from handlers.home_handler import HomeHandler
from handlers.capture_handler import CaptureHandler
from handlers.capture_stream_handler import CaptureStreamHandler
from handlers.cast_handler import CastHandler
from handlers.cast_stream_handler import CastStreamHandler


application = tornado.web.Application([
    (r"/scripts/(.*)", tornado.web.StaticFileHandler, {'path': 'scripts'}),
    (r"/", HomeHandler),
    (r"/capture", CaptureHandler),
    (r"/capture-stream", CaptureStreamHandler),
    (r"/cast/(.*)", CastHandler),
    (r"/cast-stream/(.*)", CastStreamHandler)
], **settings)

if __name__ == "__main__":
    def stop_server(signum, frame):
        log.info('Stopping server')
        loop.stop()

    signal.signal(signal.SIGINT, stop_server)

    log = get_app_logger()
    log.setLevel(options.loglevel)
    log.info('Starting Tornado {0} server'.format(tornado.version))
    log.info('Press Ctrl+C to stop')

    application.listen(options.port)
    loop = tornado.ioloop.IOLoop.current()
    loop.start()
