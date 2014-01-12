from tornado.web import url

import controllers.main

urls=[
	url(
		'/',
		controllers.main.Main,
		name='index'
	),
	url(
		'/open',
		controllers.main.Main,
		name='open'
	)
]