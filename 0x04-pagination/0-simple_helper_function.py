#!/usr/bin/env python3
"""
Pagination
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return tuple containing pagination start index and end index. """
    return (page_size * (page - 1), page * page_size)
