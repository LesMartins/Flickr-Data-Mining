#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mongoengine
import config
import csv
import pymaps

def initdb(db):
    db.drop_database(config.db_name)

class FlickrDialect(csv.Dialect):
    delimiter = ","
    quotechar = '"'
    escapechar = None
    doublequote = None
    lineterminator = "\r\n"
    quoting = csv.QUOTE_ALL
    skipinitialspace = False

def genMap():
    tmap = pymaps.Map()
    tmap.zoom = 11
    tmap.center = (45.75972, 4.84222)

    data = csv.DictReader(open(config.csv_file_name, "rb"), dialect=FlickrDialect())
    for i, row in enumerate(data):
        if i % 100 == 0:
            legend = """<ul>
            <li><strong>Legend</strong>: {}</li>
            <li><strong>Tags</strong>: {}</li>
            </ul>""".format(row['legend'], row['hashtags'])
            tmap.setpoint((row['latitude'], row['longitude'], legend))
    gmap = pymaps.PyMap(maplist=[tmap])

    return gmap.pymapjs()

if __name__ == "__main__":
    db = mongoengine.connect(config.db_name)
    initdb(db)
