#!/usr/bin/env python
#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import tornado.httpserver
import tornado.ioloop
from tornado import httpclient
import tornado.web
import tornado.options
from tornado import gen
from tornado.options import define, options
import helpers as h
import brukva
from brukva import adisp
import random
import database
from realtime import publish
import re
import urllib2
import urllib
import redis

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class CareHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('care.html')

class UWHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @adisp.process
    def post(self):
        phone = self.get_argument('phone')
        c = database.AsyncRedis.client()
        yield c.async.zrem("phone",phone)
        yield c.async.delete("weather:%s"%phone)
        self.render('uncared.html')

class WHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @adisp.process
    def post(self):
        phone = self.get_argument('phone')
        string = self.get_argument('sms', None)
        if string is None:
            string = u"您好，{weather}"
        c = database.AsyncRedis.client()
        yield c.async.zadd("phone",1,phone)
        if phone != None:
            def handle_request(response):
                if response.error:
                    print "Error:", response.error
                else:
                    print response.body
            sms = string.replace("{weather}",u"明天降温x度,记得添件衣服")
            sms = u"%s"%sms
            yield c.async.set("weather:%s"%phone,string)
        self.render('cared.html',strings = sms)

def main():
    define("port", default=8000, help="run on the given port", type=int)
    settings = {"debug": True, "template_path": "templates","static_path": "static",
           "cookie_secret": "z1DAVh+WTvyqpWGmOtJCQLETQYUznEuYskSF062J0To="}
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/",              IndexHandler),
        (r"/weather",            WHandler),
        (r"/unsub",            UWHandler),
        (r"/care",            CareHandler),
    ], **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    main()
