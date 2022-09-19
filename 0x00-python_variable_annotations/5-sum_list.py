#!/usr/bin/env python3
""" Type-annotated function sum_list which takes a list
and return its sum."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of list"""
    return sum(input_list)
