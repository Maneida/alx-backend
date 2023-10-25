#!/usr/bin env python3
"""
Module for basic dictionary in caching
"""
from base_caching import BaseCaching
from typing import Any, Union


class BasicCache(BaseCaching):
    """Basic cache dictionary class"""
    def __init__(self):
        """Initializes BasicCache class"""
        super().__init__()

    # def put(self, key: Hashable, item: Any) -> None:
    def put(self, key: Union[str, int, bytes], item: Any) -> None:
        """Adds an item to the cache"""
        # if key is not None and item is not None:
        if key and item:
            self.cache_data[key] = item

    def get(self, key: Union[str, int, bytes]) -> Any:
        """Gets an item from the cache"""
        if key:
            return self.cache_data.get(key)
        return None
