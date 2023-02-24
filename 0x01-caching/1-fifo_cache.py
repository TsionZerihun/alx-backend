#!/usr/bin/env python3
"""
import the parent BaseCaching class
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """caching using FIFO algorithm"""

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        if (key is None) or (item is None):
            pass
        elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
        else:
            print("DISCARD: {}".format(list(self.cache_data)[0]))
            self.cache_data.pop(list(self.cache_data)[0])
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data
        """
        return (self.cache_data.get(key))
