#!/usr/bin/env python3
""" Convert to tuple"""
from typing import List, Tuple, Union


def to_kv(k:str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a Tuple"""
    return Tuple(k, (v * v))
