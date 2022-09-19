#!/usr/bin/env python3
""" Type-annotated function floor which
takes a float n as argument and returns the floor of the float."""


def floor(n: float) -> float:
    """ Returns the floor of the float"""
    return float(str(n)[0:str(n).index(".")])
