#!/usr/bin/env python3
""" Basic annotations - to string """
from typing import List, Union, Tuple, Callable, Iterable, Sequence, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Return list of floats """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
