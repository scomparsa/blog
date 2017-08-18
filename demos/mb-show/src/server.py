# -*- coding:utf8 -*-

import sys
import getopt
import tornado.ioloop
import tornado.httpserver

from application import Application

class Main:

    def __init__(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "h:p:")
            for opt, value in opts:
                if opt == "-h":
                    host = value
                elif opt == "-p":
                    port = value
        except:
            print args
            self.__exit()
        print "server start at http://%s:%s" % (host, port)
        http_server = tornado.httpserver.HTTPServer(Application())
        http_server.listen(port, host)
        tornado.ioloop.IOLoop.instance().start()

    def __exit(self):
        print "please set the -h (host) -p (port) parameters\nexample : python server.py -h 127.0.0.1 -p 8000"
        exit(0)

if __name__ == "__main__":
    Main()