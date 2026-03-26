#!/usr/bin/env python3
"""Module that runs multiple coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random n times concurrently and return delays in ascending order.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []

    coroutines = [wait_random(max_delay) for _ in range(n)]

    for coro in asyncio.as_completed(coroutines):
        result = await coro
        delays.append(result)

    return delays
