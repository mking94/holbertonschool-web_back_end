#!/usr/bin/env python3
""" Convert to tuple"""
from typing import Tuple, Union


def to_kv(k:str, v: Union[int, float]) -> Tuple:
    """ Returns a Tuple"""
    return Tuple(k, (v * v))
