#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize dataset attributes"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return dataset indexed by position"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """Return deletion-resilient paginated data"""

        dataset = self.indexed_dataset()

        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert index < len(dataset)

        data = []
        current = index

        # collect page_size valid items
        while len(data) < page_size:
            if current in dataset:
                data.append(dataset[current])
            current += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current
        }
