#!/usr/bin/env python3
""" Function that insert documents in a collection """

def insert_school(mongo_collection, **kwargs):
    """ Function that insert documents in a collection """
    if mongo_collection is None:
        return None
    return mongo_collection.insert_one(kwargs).inserted_id
