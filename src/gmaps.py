#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random

#Scroll down jeune padawan, this class is no meant to be modified ^^
#Interesting code is at the bottom of the file. :p
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


    def _getIconUrlByColor(self, color):
        return 'http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|{}'.format(color)


    def _points(self):
        string = ''
        for point in self.points:
            string += """
            new google.maps.Marker({
                position: new google.maps.LatLng %s,
                map: theMap,
                icon: new google.maps.MarkerImage("%s")
            });""" % (str(point['coord']), self._getIconUrlByColor(point['color']))

        return string


    def _circles(self):
        string = ''
        for i, circle in enumerate(self.circles):
            string += """
            var circle%d = new google.maps.Circle({
                center: new google.maps.LatLng %s,
                map: theMap,
                radius: %d,
                fillColor: '%s',
                clickable: true
            });""" % (i, str(circle['coord']), circle['radius'], circle['color'])

            if 'info' in circle:
                string += """
                 var infowincircle%d = new google.maps.InfoWindow({
                    content: "%s"
                });
                google.maps.event.addListener(
                circle%d, 'click', function() {
                    infowincircle%d.setPosition(circle%d.getCenter());
                    infowincircle%d.open(theMap);
                });""" % (i, circle['info'], i, i, i, i)

        return string

def randomColor():
    r = lambda: random.randint(0, 255)
    return '%02X%02X%02X' % (r(),r(),r())


#Here is the intersting code to generate the map.
def genMap(centers, data):
    myMap = GMaps()

#We want to center the map on Lyon
    myMap.center = (45.75972, 4.84222)
    myMap.zoom = 11

    #We first add circles (centers of clusters)
    for i, row in enumerate(centers):
        row['color'] = randomColor()
        myMap.circles.append({
            'coord': (float(row['x']), float(row['y'])),
            'radius': 10 * math.sqrt(row['number']),
            'color': '#%s' % (row['color']),
            'info': "<h3>Cluster {}</h3><br />Number of elements: <strong>{}</strong>".format(row['cluster'], row['number'])
            })

    #And we add 1/100 of the points.
    for i, row in enumerate(data):
        if i % 100 == 0:
            myMap.points.append({
                'coord': (float(row['latitude']), float(row['longitude'])),
                'color': centers[row['cluster']]['color']
                })

    return myMap.js()
