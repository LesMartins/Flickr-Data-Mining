#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MeanShift, estimate_bandwidth, KMeans
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
    bandwidth = estimate_bandwidth(X, quantile=0.01, n_samples=1000)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True, cluster_all=False, min_bin_freq=15)
    ms.fit(X)

    labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    labels_unique = numpy.unique(labels)
    n_clusters_ = len(labels_unique) - 1

#We generate the list of dicts representing the center of our clusters.
#cluster is the ID of the cluster
#x and y are the coordinates for the center of this cluster
#number is the number of points in that cluster
    centers = list()
    for i, row in enumerate(cluster_centers):
        centers.append({'cluster': i, 'x': row[0], 'y': row[1], 'number': labels.tolist().count(i)})

    points = list()
    for i, row in enumerate(X):
#-1 means that the point doesn't belong to any cluster (has been rejected).
#So we don't want to return these points and throw them away.
        if labels[i] != -1:
            l2[i]['cluster'] = labels[i]
            points.append(l2[i])

    return centers, points



def kmeans():
    l1, l2 = list(), list()

    X = parser.parseFile(config.csv_file_name)
    for i, row in enumerate(X):
        sublist = [float(row['latitude']), float(row['longitude'])]
        l1.append(sublist)
        l2.append(row)

    ss = StandardScaler(with_mean=False, with_std=False)
    X = ss.fit_transform(l1)
    km = KMeans(n_clusters=100, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances=True, verbose=0, random_state=None, copy_x=True, n_jobs=1)
    km.fit(X)

    labels = km.labels_
    cluster_centers = km.cluster_centers_
    labels_unique = numpy.unique(labels)
    n_clusters_ = len(labels_unique) - 1

#We generate the list of dicts representing the center of our clusters.
#cluster is the ID of the cluster
#x and y are the coordinates for the center of this cluster
#number is the number of points in that cluster
    centers = list()
    for i, row in enumerate(cluster_centers):
        centers.append({'cluster': i, 'x': row[0], 'y': row[1], 'number': labels.tolist().count(i)})

    points = list()
    for i, row in enumerate(X):
#-1 means that the point doesn't belong to any cluster (has been rejected).
#So we don't want to return these points and throw them away.
        if labels[i] != -1:
            l2[i]['cluster'] = labels[i]
            points.append(l2[i])

    return centers, points

