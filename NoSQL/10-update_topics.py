#!/usr/bin/env python3
"""
Module to update school topics in a MongoDB collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the name
    """
    # Use update_many to change all documents with the matching name
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
