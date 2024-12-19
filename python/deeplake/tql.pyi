"""
TQL api, to run queries on data containers.
"""

from __future__ import annotations

from typing import Callable, Any

__all__ = [
    "register_function",
]

def register_function(function: typing.Callable) -> None:
    """
    Registers the given function in TQL, to be used in queries.
    TQL interacts with Python functions through `numpy.ndarray`. The Python function
    to be used in TQL should accept input arguments as numpy arrays and return numpy array.

    Examples:
        ```python
        def next_number(a):
            return a + 1
        
        deeplake.tql.register_function(next_number)
        
        r = ds.query("SELECT * WHERE next_number(column_name) > 10")
        ```
    """