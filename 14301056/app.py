# coding: utf-8
from __future__ import unicode_literals
from wsgiref import simple_server


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    str = environ['PATH_INFO'][1:]
    print str

    # return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    # return ['Hello world from a RAPOWSGI application!\n']