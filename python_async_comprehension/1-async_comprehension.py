#!/usr/bin/env python3
"""
Module to measure the runtime of four parallel async comprehensions.
"""

import asyncio
import time
from typing import Coroutine

async_comprehension = __import__('1-async_comprehension').async_comprehension
