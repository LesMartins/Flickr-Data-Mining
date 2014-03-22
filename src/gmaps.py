#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class GMaps:

    def __init__(self):
        self.center = (0, 0)
        self.points = []
        self.circles = []
        self.zoom = 1
        self.div_id = 'map'

    def js(self):
        return """
    <script type="text/javascript">
        function init()
        {
            var mycenter = new google.maps.LatLng %s;
            var options = {
                zoom: %d,
                center: mycenter
            }
            var theMap = new google.maps.Map(document.getElementById('%s'), options);

            %s

            %s
        }
        google.maps.event.addDomListener(window, 'load', init);
    </script>
    """ % (str(self.center), self.zoom, self.div_id, self._points(), self._circles())

    def _points(self):
        string = ''
        for point in self.points:
            string += """
            new google.maps.Marker({
                position: new google.maps.LatLng %s,
                map: theMap
            });""" % (str(point))

        return string

    def _circles(self):
        string = ''
        for circle in self.circles:
            string += """
            new google.maps.Circle({
                center: new google.maps.LatLng %s,
                map: theMap,
                radius: %d
            });""" % (str(circle['coord']), circle['radius'])

        return string



def genMap(centers, data):
    myMap = GMaps()
    myMap.center = (45.75972, 4.84222)
    myMap.zoom = 11

    for i, row in enumerate(centers):
        myMap.circles.append({
            'coord': (float(row['x']), float(row['y'])),
            'radius': 10 * math.sqrt(row['number'])
            })

    return myMap.js()
