#!/usr/bin/env python3
"""Module that defines task_wait_n coroutine using asyncio tasks"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple asynchronous tasks concurrently and return
    the list of delays in ascending order.

    Args:
        n (int): number of tasks to run
        max_delay (int): maximum delay value

    Returns:
        List[float]: sorted list of delays
    """
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(task_wait_random(max_delay))
        tasks.append(task)

    delays = []

    for task in tasks:
        result = await task
        delays.append(result)

    return sorted(delays)
