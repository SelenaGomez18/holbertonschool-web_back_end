def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
    """Return deletion-resilient page"""

    dataset = self.indexed_dataset()

    if index is None:
        index = 0

    assert isinstance(index, int) and index >= 0

    data = []
    current = index

    # collect valid items
    while len(data) < page_size and current <= max(dataset.keys()):
        if current in dataset:
            data.append(dataset[current])
        current += 1

    return {
        "index": index,
        "data": data,
        "page_size": len(data),
        "next_index": current
    }
