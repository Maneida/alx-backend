#!/usr/bin/env python3
"""This module showcases cache retaining policies/algorithms"""
from typing import Any, Union
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implements an LFU caching system"""
    def __init__(self):
        super().__init__()
        self.hits = {}

    def put(self, key: Union[str, int, bytes], item: Any) -> None:
        """Adds an item to the cache using the LFU algorithm"""
        if key and item:
            # Add new item to cache and update its number of hits
            self.cache_data[key] = item
            self.__hit__(key)

            # Remove least frequently used item if LFU queue is full
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                # Create tuples of keys and number of hits -> (hits, key)
                hits = sorted([(self.hits[key], key)
                               for key in self.hits.keys()])
                # Grab key from tuple with the lowest hits
                lfu = hits[0][1]
                # Skip over current key if it is the lfu
                lfu = hits[1][1] if lfu == key else lfu

                # Delete key from cache and discard its number of hits
                del self.cache_data[lfu]
                del self.hits[lfu]
                print(f'DISCARD: {lfu}')

    def get(self, key: Union[str, int, bytes]) -> Any:
        """Gets an item from the cache using LFU algorithm"""
        if key:
            # Update number of hits for item in LFU cache
            self.__hit__(key)

            return self.cache_data.get(key)
        return None

    def __hit__(self, key: Union[str, int, bytes]) -> None:
        """Increments the number of hits for an item in the LFU cache"""
        if self.cache_data.get(key):
            self.hits.setdefault(key, 0)
            self.hits[key] += 1
