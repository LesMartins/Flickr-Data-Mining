#!/usr/bin/env python
# -*- coding: utf-8 -*-

class GMaps:

    def __init__(self):
        self.center = (0, 0)
        self.points = []
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
        }
        google.maps.event.addDomListener(window, 'load', init);
    </script>
    """ % (str(self.center), self.zoom, self.div_id)


def genMap(centers, data):
    myMap = GMaps()
    myMap.center = (45.75972, 4.84222)
    myMap.zoom = 11
    return myMap.js()
