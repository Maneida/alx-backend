#!/usr/bin/env python3
"""Module for FIFO Caching"""
from typing import Any, Union
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implements a FIFO/queue caching system"""
    def __init__(self):
        """Initializes FIFOCache class"""
        super().__init__()

    def put(self, key: Union[str, int, bytes], item: Any) -> None:
        """Adds an item to the cache using the FIFO algorithm (queue)"""
        if key and item:
            # Delete key if it exists and added to bottom of queue
            if self.cache_data.get(key):
                del self.cache_data[key]

            # Remove first item in cache if queue is full
            if len(self.cache_data.keys()) >= self.MAX_ITEMS:
                last = list(self.cache_data.keys())[0]
                del self.cache_data[last]
                print(f'DISCARD: {last}')

            # Add new item to end/bottom of queue
            self.cache_data[key] = item

    def get(self, key: Union[str, int, bytes]) -> Any:
        """Gets an item from the cache"""
        if key:
            return self.cache_data.get(key)
        return None
