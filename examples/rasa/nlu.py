#!/usr/bin/env python3

import os

import tornado.ioloop
import tornado.web

from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.train import do_train


class InterpretHandler(tornado.web.RequestHandler):
    def get(self):
        interpreter = InterpretHandler.interpreter
        query = self.get_query_argument('query')
        result = interpreter.parse(query)
        self.write(result)


def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(script_dir, 'data')
    os.chdir(data_dir)
    nlu_config = RasaNLUConfig(filename='nlu_config.json')

    trainer, interpreter, persist_path = do_train(nlu_config)
    InterpretHandler.interpreter = interpreter

    static_dir = os.path.join(script_dir, 'www')
    webapp = tornado.web.Application([
        (r'/interpret', InterpretHandler),
        (r'/(.*)', tornado.web.StaticFileHandler, {
            'path': static_dir,
            'default_filename': 'index.html',
        }),
    ])

    port = 8080
    webapp.listen(port)
    print('listening on {}'.format(port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
