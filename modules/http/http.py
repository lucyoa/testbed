#!/usr/bin/env python

import modules.http.scenarios as scenarios
import SimpleHTTPServer
import BaseHTTPServer

PORT_NUMBER = 8080


class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        scenarios.scenarios[self.server.scenario](self)
    def do_POST(self):
        print(self.path)
        scenarios.scenarios[self.server.scenario](self)


class HttpServer(BaseHTTPServer.HTTPServer):
    def serve_forever(self, scenario):
        self.scenario = scenario
        self.stop = False

        while self.stop == False:
            self.handle_request()


class Http(object):
    def __init__(self, scenario):
        self.scenario = scenario
        server = HttpServer(('', PORT_NUMBER), HttpRequestHandler)
        print("Started httpserver on port {}".format(PORT_NUMBER))
        server.serve_forever(scenario)
