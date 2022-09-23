#!/usr/bin/python3
""" LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    This class will inherit self.cache_data from BaseCashing
    """
    def __init__(self):
        """
        Init from BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds key value pairs to self.cache_data
        """
        if key is not None and item is not None:
            keyList = list(self.cache_data)[0:]
            if key in keyList:
                del self.cache_data[key]
                keyList.remove(key)
            if (len(keyList) + 1) > BaseCaching.MAX_ITEMS:
                remove = keyList.pop()
                print("DISCARD: " + remove)
                del self.cache_data[remove]
            self.cache_data[key] = item
            keyList.append(key)

        else:
            pass

    def get(self, key):
        """
        Retrieves items from self.cache_data by key
        """
        try:
            return self.cache_data[key]
        except Exception:
            pass
