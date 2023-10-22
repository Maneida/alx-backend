#!/usr/bin/env python3
"""
Module for simple pagination
"""
import csv
import math
from typing import List, Dict


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
        """ Gets the page based on page size parameters
        """
        try:
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0

            start_index, end_index = index_range(page, page_size)

            if (start_index or end_index) > len(self.dataset()):
                return []
            else:
                return self.dataset()[start_index:end_index]
        except AssertionError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Hypermedia pagination
        Args:
            page (int, optional):  Defaults to 1.
            page_size (int, optional):  Defaults to 10.

        Returns:
            Dict: with key-value pairs
                page_size: the length of the returned dataset page
                page: the current page number
                data: the dataset page (equivalent to return from
                      previous task)
                next_page: number of the next page, None if no next page
                prev_page: number of the previous page, None if no
                           previous page
                total_pages: the total number of pages in the dataset
                             as an integer
        """
        data = self.get_page(page, page_size)
        total_pages = (math.ceil(len(self.dataset())) if page_size == 0
                       else math.ceil(len(self.dataset()) / page_size))
        next_page = (page + 1) if (page + 1) <= total_pages else None
        prev_page = (page - 1) if page > 1 else None

        return {"page_size": page_size, "page": page, "data": data,
                "next_page": next_page, "prev_page": prev_page,
                "total_pages": total_pages}
