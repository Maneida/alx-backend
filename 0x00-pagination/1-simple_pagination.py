#!/usr/bin/env python3
"""
Module for simple pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int, **kwargs) -> tuple:
    """
    Function named index_range that takes
    two integer arguments page and page_size

    Returns:
    tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters
    """
    page -= 1
    start_index = page * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

class Server:
    """Server class to paginatte a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Gets the page based on pagesize parameters
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        '''if page or page_size <= 0:
            raise AssertionError'''
        
        start_index, end_index = index_range(page, page_size)

        if (start_index or end_index) > len(self.dataset()):
            return []
        else:
            return self.dataset()[start_index:end_index]
