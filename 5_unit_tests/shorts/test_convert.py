#!/usr/bin/env python

import pytest
from convert import convert


def test_int_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000


def test_error():
    with pytest.raises(TypeError):
        convert("1")
        # Expecting that trying to convert a string
        # (even of a number) would raise an error


def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)
    # approx allows the necessary approximation
    # that is always needed when dealing with floats
    # I can also adjust the tolerance with abs=0.1, abs=1e-5... as desired
