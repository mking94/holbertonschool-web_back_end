#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Return list of wait_random
    """
    list_random = []
    for _ in range(n):
        list_random.append(await asyncio.sleep(max_delay))
    return sorted(list_random)
