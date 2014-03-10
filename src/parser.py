#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mongoengine
import config
import csv

def initdb(db):
    db.drop_database(config.db_name)

class FlickrDialect(csv.Dialect):
    delimiter = "\t"
    quotechar = None
    escapechar = None
    doublequote = None
    lineterminator = "\r\n"
    quoting = csv.QUOTE_NONE
    skipinitialspace = False

def parse():
    data = csv.DictReader(open(config.csv_file_name, "rb"), dialect=FlickrDialect())

if __name__ == "__main__":
    db = mongoengine.connect(config.db_name)
    initdb(db)
    parse()
