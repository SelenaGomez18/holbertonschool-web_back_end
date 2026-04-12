#!/usr/bin/env python3
"""
Module to find schools by a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic
    """
    # Filter documents where 'topics' list contains the specified topic
    return list(mongo_collection.find({"topics": topic}))
