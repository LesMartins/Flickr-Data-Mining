#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MeanShift
import csv
import config
import parser

def meanShift():
    l1, l2 = list(), list()

    data = csv.DictReader(open(config.csv_file_name, "rb"), dialect=parser.FlickrDialect())
    for i, row in enumerate(data):
        if i % 1 == 0:
            #attention a prendre un nombre suffisant de donnee pour que meanshift marche
            sublist = [float(row['latitude']), float(row['longitude'])]
            l1.append(sublist)
            l2.append(row)


    ss = StandardScaler(with_mean=False, with_std=False)
    test = ss.fit_transform(l1)
    ms = MeanShift(bandwidth=0.001, bin_seeding=True, cluster_all=False, min_bin_freq=15)
    ms.fit(test)


meanShift()
