#!/usr/bin/env python

import pytest
from plates import is_valid


def test_length():
    assert is_valid("CS50505") == False
    assert is_valid("CS5050") == True


def test_first_chars():
    assert is_valid("CS") == True
    assert is_valid("50") == False


def test_char_spec():
    assert is_valid("CS;") == False


def test_orden_char():
    assert is_valid("CS50C0") == False


def test_zero_placement():
    assert is_valid("CS0") == False


# def test_crash():
#     assert is_valid(0) == "Check if pytest really works"
