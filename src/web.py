#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import parser
import cluster

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/map")
def map():
    the_map = parser.genMap(*cluster.meanShift())
    return render_template("map.html", the_map=the_map)

if __name__ == "__main__":
    app.run(debug=True)
