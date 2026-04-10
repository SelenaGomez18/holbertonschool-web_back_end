#!/usr/bin/env python3
"""
Module that provides a Server class for deletion-resilient pagination.
"""

import csv
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names
    with deletion-resilient hypermedia pagination.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """
        Initialize the Server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset.

        Returns:
            List[List]: The dataset loaded from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Return the dataset indexed by position.

        Returns:
            Dict[int, List]: Dataset indexed by integer keys.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Return a page of the dataset using deletion-resilient pagination.

        Args:
            index (int): Starting index of the page.
            page_size (int): Number of items per page.

        Returns:
            Dict: A dictionary containing:
                - index (int): Current start index
                - data (List[List]): Page data
                - page_size (int): Number of items returned
                - next_index (int): Next index to query
        """
        dataset = self.indexed_dataset()

        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0 and index < len(dataset)

        data = []
        current_index = index

        while len(data) < page_size:
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current_index
        }
