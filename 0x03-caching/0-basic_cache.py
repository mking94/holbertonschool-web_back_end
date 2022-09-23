#!/usr/bin/env python3
""" BasicCache """

BaseCaching = __import__('BaseCaching')

class BasicCache(BaseCaching):
    """ BasicCache module """
    def put(self, key, item):
        """ Put the key and item"""
        if (key != None or item != None):
            self.cache_data[key] = item
    def get(self, key):
        """ Get the cache data"""
        if key is not None and key not in self.cache_data:
            return self.cache_data[key]
        return None
