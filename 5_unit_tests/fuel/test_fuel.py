#!/usr/bin/env python

import pytest
from fuel import convert, gauge


def test_convert():
    assert convert(["2", "4"]) == 50
    with pytest.raises(ValueError):
        convert(["4", "-1"])
    with pytest.raises(ValueError):
        convert(["-1", "4"])
    with pytest.raises(TypeError):
        convert(["f", "4"])
    with pytest.raises(TypeError):
        convert(["4", "f"])
    # with pytest.raises(ZeroDivisionError):
    #     convert(["4", "0"])


# def test_gauge(): ...
