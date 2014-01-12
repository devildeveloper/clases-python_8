import tornado.web
import tornado.escape

class RequestHandler(tornado.web.RequestHandler):
	def __init__(self,application,request,**kwargs):
		super(RequestHandler,self).__init__(application,request,**kwargs)

	def render_string(self,template_name,**kwargs):
		kwargs.update({'handler':self})
		return self.application._template_env.get_template(template_name).render(**kwargs)

	def render (self,template_name,**kwargs):
		self.finish(self.render_string(template_name,**kwargs))

