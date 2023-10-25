#!/usr/bin/env python3
"""Module for LIFO Caching"""
from typing import Any, Union
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implements a LIFO/stack caching system"""
    def __init__(self):
        """ Initializes LIFOCache class"""
        super().__init__()

    def put(self, key: Union[str, int, bytes], item: Any) -> None:
        """Adds an item to the cache using the LIFO algorithm (stack)"""
        if key and item:
            # Delete key if it exists so it's added to top of stack
            if self.cache_data.get(key):
                del self.cache_data[key]

            # Remove last item in cache if stack is full
            if len(self.cache_data.keys()) >= self.MAX_ITEMS:
                last = list(self.cache_data.keys())[-1]
                del self.cache_data[last]
                print(f'DISCARD: {last}')

            # Add new item to top of stack
            self.cache_data[key] = item

    def get(self, key: Union[str, int, bytes]) -> Any:
        """Gets an item from the cache"""
        if key:
            return self.cache_data.get(key)
        return None
