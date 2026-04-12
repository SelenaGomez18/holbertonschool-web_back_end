#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """
    List all documents in a collection
    """
    # Return empty list if no documents found
    if mongo_collection is None:
        return []

    # Get all documents from the collection
    return list(mongo_collection.find())
