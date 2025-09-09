#!/usr/bin/env python

import pytest

from calculator import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    # assert square(0) == "Check if pytest really works"
