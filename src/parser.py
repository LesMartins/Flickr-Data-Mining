#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mongoengine
import config

def initdb(db):
    db.drop_database(config.db_name)

if __name__ == "__main__":
    db = mongoengine.connect(config.db_name)
    initdb(db)
