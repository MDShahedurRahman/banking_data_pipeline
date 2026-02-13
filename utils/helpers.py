# utils/helpers.py

import os


def create_folder(path):
    """
    Ensures output directories exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)
