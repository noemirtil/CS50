#!/usr/bin/env python

import pytest
from um import count


def test_count_cs50():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_count_between():
    assert count("Mummy") == 0
    assert count("?um?") == 1


def test_count_beginning():
    assert count("Umbrella") == 0
    assert count("Um, mummy") == 1


def test_count_end():
    assert count("Barnum") == 0
    assert count("Barnum, um") == 1
    assert count("-um") == 1
