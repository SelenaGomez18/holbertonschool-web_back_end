#!/usr/bin/env python3
"""
Este módulo proporciona una función para listar todos los documentos
de una colección de MongoDB utilizando PyMongo.
"""


def list_all(mongo_collection):
    """
    Lista todos los documentos en una colección.

    Args:
        mongo_collection: Objeto de colección de pymongo.

    Returns:
        Una lista con todos los documentos encontrados en la colección.
        Si no hay documentos, devuelve una lista vacía.
    """
    # Usamos .find() sin argumentos para obtener todos los documentos
    documents = list(mongo_collection.find())

    return documents
