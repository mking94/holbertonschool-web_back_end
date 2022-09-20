#!/usr/bin/env python3
''' Description: asynchronous coroutine that takes in an integer argument
                 (max_delay, with a default value of 10)
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Return a ramdom number after wait"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
