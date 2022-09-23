#!/usr/bin/env python3

""" BasicCache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
   """ BasicCache module """

   def put(self, key, item):
        """ Put the key and item"""
        if (key is not None or item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """ Get the cache data"""
        if key is None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
