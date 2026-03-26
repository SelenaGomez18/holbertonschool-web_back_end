#!/usr/bin/env python3
"""Module that runs multiple asyncio tasks concurrently."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute task_wait_random n times concurrently and return delays in ascending order.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
