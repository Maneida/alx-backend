#!/usr/bin/env python3
"""
Module for a helper function named index_range that takes
two integer arguments page and page_size.
"""


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
