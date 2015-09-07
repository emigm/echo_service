'''Echo HTTP handler'''
import tornado.gen
import tornado.web


class EchoHandler(tornado.web.RequestHandler):  # pylint: disable=R0904
    '''Handle echo operations'''

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    def post(self):
        '''POST method'''

        self.logger = self.settings['logger']

        self.logger.info('Method: {method}'.format(method=self.request.method))
        self.logger.info('Path: {path}'.format(path=self.request.path))
        self.logger.info('Query: {query}'.format(query=self.request.query))
        self.logger.info('Body: {body}'.format(body=self.request.body))

        message = self.request.body.decode('utf-8')

        self.set_status(200)
        self.write('You sent me:' + message)
        self.finish()
