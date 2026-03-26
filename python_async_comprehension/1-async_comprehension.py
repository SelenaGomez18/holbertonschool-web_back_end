#!/usr/bin/env python3
"""Module that defines async comprehension coroutine"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension.

    This coroutine uses async comprehension to gather values
    from async_generator and returns them as a list.

    Returns:
        List[float]: list of 10 random numbers
    """
    return [i async for i in async_generator()]
