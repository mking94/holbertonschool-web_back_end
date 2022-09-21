#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio

async_comprehension = __import__(
    '1-async_comprehension.py').async_comprehension


async def async_comprehension():
    """ Collect 10 random numbers using an async
    comprehensing over async_generator """
    for i in range(4):
        asyncio.gather(async_comprehension)
