#!/usr/bin/env python

import pytest
from numb3rs import validate


def test_validate():
    assert validate("cat") == False
    assert validate("10") == False
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False
