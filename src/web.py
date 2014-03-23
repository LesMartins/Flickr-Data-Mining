#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import gmaps
import cluster

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

#URL /map now generates a map with meanshift.
#We could add another route and user another clustering algo.
@app.route("/map")
def map():
    the_map = gmaps.genMap(*cluster.meanShift())
    return render_template("map.html", the_map=the_map)


@app.route("/othermap")
def othermap():
    the_map = gmaps.genMap(*cluster.kmeans())
    return render_template("map.html", the_map=the_map)

if __name__ == "__main__":
    app.run(debug=True)
