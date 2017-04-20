#!/usr/bin/env python

import sys
from modules.http.http import Http


def main():
    module = sys.argv[1]
    scenario = int(sys.argv[2])

    if module == 'http':
        Http(scenario)


if __name__ == '__main__':
    main()
