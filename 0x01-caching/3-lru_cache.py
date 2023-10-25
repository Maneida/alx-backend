"""Module showcasing LRU Caching"""
from typing import Any, Union
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implements an LRU caching system"""
    def __init__(self):
        """ Initializes LRUCache class"""
        super().__init__()

    def put(self, key: Union[str, int, bytes], item: Any) -> None:
        """Adds an item to the cache using the LRU algorithm (a queue)"""
        if key and item:
            # Delete key if it exists so it's added to bottom of queue
            if self.cache_data.get(key):
                del self.cache_data[key]

            # Remove first item in cache if LRU queue is full
            if len(self.cache_data.keys()) >= self.MAX_ITEMS:
                last = list(self.cache_data.keys())[0]
                del self.cache_data[last]
                print(f'DISCARD: {last}')

            # Add new item to bottom of LRU queue
            self.cache_data[key] = item

    def get(self, key: Union[str, int, bytes]) -> Any:
        """Gets an item from the cache and moves it to back of LRU queue"""
        val = self.cache_data.get(key)
        if key and val:
            # Move key to bottom of LRU queue
            self.put(key, val)
            return val
        return None
