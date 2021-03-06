#!/usr/bin/env python
# -*- coding: utf-8 -*-
from main import *

def test__00__init():
    """
    >>> print valves
    xxx
    >>> for id in range(8):
    ...     print valves[id]
    ...     valves[id].water()
    ...     sleep(0.5)
    ...     valves[id].nowater()
    ...     sleep(0.5)
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
