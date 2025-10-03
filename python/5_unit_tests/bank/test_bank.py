#!/usr/bin/env python

import pytest
from bank import value


def test_lower():
    assert value("hello") == 0
    assert value("ola") == 100
    assert value("hey") == 20


def test_upper():
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("OLA") == 100
    assert value("HEY") == 20


# def test_crash():
#     assert shorten("tibidabo") == "Check if pytest really works"
