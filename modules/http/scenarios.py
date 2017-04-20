#!/usr/bin/env python

import time
import os


def no_response(s):
    s.wfile.write("")


def trash(s):
    s.wfile.write(os.urandom(100))


def no_found(s):
    s.send_response(404)


def found(s):
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()

    s.wfile.write("Something")


def redirect(s):
    s.send_response(302)
    s.end_headers()


def timeout(s):
    time.sleep(128)


scenarios = {
    1: no_response,
    2: trash,
    3: no_found,
    4: found,
    5: redirect,
    6: timeout,
}
