#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Generator a random value between 0 and 10 every second """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
