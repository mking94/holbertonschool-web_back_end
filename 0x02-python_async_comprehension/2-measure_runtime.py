#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension.py').async_comprehension


async def measure_runtime() -> float:
    """ Execute async_comprehension """
    start - time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time.time()
    time_t = end_time - start_time
    return time_t
