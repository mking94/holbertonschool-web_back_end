#!/usr/bin/env python3

""" BasicCache """

BaseCaching = __import__('BaseCaching').BaseCaching

class BasicCache(BaseCaching):
""" BasicCache module """
    def put(self, key, item):
        """ Put the key and item"""
        if (key != None or item != None):
            self.cache_data[key] = item
    def get(self, key):
        """ Get the cache data"""
        if (key is None or key not in self.cache_data.keys()):
            return None
        else :
            return self.cache_data[key]
