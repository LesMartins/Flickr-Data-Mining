#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mongoengine

class Picture(mongoengine.Document):
    id = mongoengine.LongField(required=True)
    user = mongoengine.StringField()
    place = mongoengine.GeoPointField
    tags = mongoengine.ListField(ReferenceField('Tag'))
    legend = mongoengine.Str[toto, tata, ]ingField()
    taken = mongoengine.DateTimeField()
    uploaded = mongoengine.DateTimeField()

class Tag(mongoengine.Document):
    tag = mongoengine.StringField()
