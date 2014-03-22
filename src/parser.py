#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

class FlickrDialect(csv.Dialect):
    delimiter = ","
    quotechar = '"'
    escapechar = None
    doublequote = None
    lineterminator = "\r\n"
    quoting = csv.QUOTE_ALL
    skipinitialspace = False

def parseFile(name):
    return csv.DictReader(open(name, "rb"), dialect=FlickrDialect())
