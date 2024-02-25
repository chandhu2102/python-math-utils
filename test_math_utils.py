from math_utils import MathUtils
import pytest

math_utils = MathUtils()

def test_add():
    assert math_utils.add(2, 3) == 5
    assert math_utils.add(-2, 1) == -1

def test_subtract():
    assert math_utils.subtract(3, 2) == 1
    assert math_utils.subtract(-2, 1) == -3

def test_multiply():
    assert math_utils.multiply(2, 3) == 6
    assert math_utils.multiply(-2, 1) == -2

def test_divide():
    assert math_utils.divide(6, 3) == 2.0
    assert math_utils.divide(2, -1) == -2.0
    assert math_utils.divide(5, 0) == -1.0
