from controllers import RequestHandler
import tornado.escape
import settings
import os

class Main(RequestHandler):
	def get(self):
		self.render('index.html',archivos=getattr(settings,'ARCHIVOS'))
	def post(self):
		archivo=self.get_argument('archivo')
		if archivo.endswith('.html'):
			os.system('vi '+ getattr(settings,'MEDIA_PATH')+'/'+archivo)