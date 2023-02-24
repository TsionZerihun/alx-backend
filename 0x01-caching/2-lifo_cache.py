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
        if (key is None) or (item is None):
            pass
        elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
        else:
            print("DISCARD: {}".format(list(self.cache_data)[0]))
            self.cache_data.popitem()
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data
        """
        if (key is None) or (key not in self.cache_data):
            return None
        else:
            return (self.cache_data.get(key))
