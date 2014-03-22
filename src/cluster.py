#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MeanShift, estimate_bandwidth
import csv
import config
import numpy
import parser

def meanShift():
    l1, l2 = list(), list()

    X = parser.parseFile(config.csv_file_name)
    for i, row in enumerate(X):
        #attention a prendre un nombre suffisant de donnee pour que meanshift marche
        sublist = [float(row['latitude']), float(row['longitude'])]
        l1.append(sublist)
        l2.append(row)

    ss = StandardScaler(with_mean=False, with_std=False)
    X = ss.fit_transform(l1)
    bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=1000)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True, cluster_all=False, min_bin_freq=15)
    ms.fit(X)

    labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    labels_unique = numpy.unique(labels)
    n_clusters_ = len(labels_unique) - 1

    centers = list()
    for i, row in enumerate(cluster_centers):
        centers.append({'cluster': i, 'x': row[0], 'y': row[1]})

    points = list()
    for i, row in enumerate(X):
        if labels[i] != -1:
            l2[i]['cluster'] = labels[i]
            points.append(l2[i])

    return centers, points
