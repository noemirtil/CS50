#!/usr/bin/env python

import pytest

from hello import say_hello


def test_default():
    assert say_hello() == "Hello, world"


def test_argument():
    assert say_hello("David") == "Hello, David"


def test_crash():
    assert say_hello() == "Check if pytest really works"
