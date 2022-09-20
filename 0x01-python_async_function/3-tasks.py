#!/usr/bin/env python3
"""
Module delay
"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Wait task.
    """
    delay_task = asyncio.create_task(wait_random(max_delay))
    return delay_task
