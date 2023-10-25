"""Module showcasing MRU Caching"""
from typing import Any, Union
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implements an MRU caching system"""
    def __init__(self):
        """ Initializes MRUCache class"""
        super().__init__()

    def put(self, key: Union[str, int, bytes], item: Any) -> None:
        """Adds an item to the cache using the MRU algorithm (a stack)"""
        if key and item:
            # Delete key if it exists so it's added to top of stack
            if self.cache_data.get(key):
                del self.cache_data[key]

            # Remove first item in cache if LRU stack is full
            if len(self.cache_data.keys()) >= self.MAX_ITEMS:
                last = list(self.cache_data.keys())[-1]
                del self.cache_data[last]
                print(f'DISCARD: {last}')

            # Add new item to top of stack
            self.cache_data[key] = item

    def get(self, key: Union[str, int, bytes]) -> Any:
        """Gets an item from the cache and moves it to back of LRU queue"""
        val = self.cache_data.get(key)
        if key and val:
            # Move key to top of MRU stack
            self.put(key, val)
            return val
        return None
