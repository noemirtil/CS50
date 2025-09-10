#!/usr/bin/env python

import pytest

from twttr import shorten


def test_shorten():
    assert shorten("aaaa") == ""
    assert shorten("AAAA") == ""
    assert shorten("1111") == "1111"
    assert shorten("....") == "...."
    assert shorten("bbbb") == "bbbb"
    assert shorten("tibidabo1..2") == "tbdb1..2"


# def test_crash():
#     assert shorten("tibidabo") == "Check if pytest really works"
