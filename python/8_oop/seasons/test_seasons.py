#!/usr/bin/env python

import pytest
from datetime import date
from seasons import check_birthdate

# from seasons import count_minutes


def test_check_birthdate():
    assert check_birthdate("1994-03-24") == date(1994, 3, 24)
    assert check_birthdate("1994-04-23") != date(1994, 3, 24)
    # assert not check_birthdate("January 1, 1999") == date(1994, 3, 24)


# def test_error():
#     with pytest.raises(ValueError):
#         convert("9 AM5 PM")
#     with pytest.raises(ValueError):
#         convert("9:00 AM to 5:60 PM")
