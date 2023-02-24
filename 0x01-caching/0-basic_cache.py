##!/usr/bin/env python3
"""
import the parent BashCashing class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
        - xy
        - xy
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ add key value pair in to the dict cache_data
        """
        if (key is None) or (item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data
        """
        if (key is None) or (key not in self.cache_data):
            return None
        else:
            return (self.cache_data.get(key))
