import tornado
from tornado.options import define,options,parse_command_line
from jinja2 import Environment ,FileSystemLoader

import settings
from urls import urls

global_settings = {}


class Application(tornado.web.Application):
	def __init__(self,handlers=None,defaul_host='',transforms=None,wsgi=False,**settings):
		super(Application,self).__init__(handlers,defaul_host,transforms,wsgi,**settings)
		self._template_env=Environment(
			loader=FileSystemLoader(self.settings.get('template_path')),
			auto_reload=self.settings.get('debug')
		)
for setting in dir(settings):
	if setting.isupper():
		global_settings.update({setting.lower():getattr(settings,setting)})


if __name__ == '__main__':
	define('host',default='127.0.0.1',help='host address to listen options')
	define('port',default=8888,type=int,help='port to listen on')

	parse_command_line()

	application=Application(urls,**global_settings)
	application.listen(options.port,options.host)
	tornado.ioloop.IOLoop.instance().start()