#!/usr/bin/env python3
"""
import the parent BaseCaching class
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ caching using FIFO algorithm
    """
    def __init__(self):
        """ Initialization
        """
        super().__init__()

    def put(self, key, item):
        """
        add key value pair in to the dict cache_data
        """
        if (key is not None) and (item is not None):
            if key not in self.cache_data:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    print("DISCARD: {}".format(self.cache_data.popitem()[0]))
                    #self.cache_data.popitem()[0]
            else:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data
        """
        if (key is None) or (key not in self.cache_data):
            return None
        else:
            return (self.cache_data.get(key))
