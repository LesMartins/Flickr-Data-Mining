#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymaps

def genMap(centers, data):
    tmap = pymaps.Map()
    tmap.zoom = 11
    tmap.center = (45.75972, 4.84222)

    for i, row in enumerate(data):
        if i % 100 == 0:
            legend = """<ul>
            <li><strong>Legend</strong>: {}</li>
            <li><strong>Tags</strong>: {}</li>
            </ul>""".format(row['legend'], row['hashtags'])
            tmap.setpoint((row['latitude'], row['longitude'], legend))
    gmap = pymaps.PyMap(maplist=[tmap])

    return gmap.pymapjs()
