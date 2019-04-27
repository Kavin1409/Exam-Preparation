import pytest
from pytest import raises
import random
import math
from simplemaths import SimpleMaths as sm

integer = random.randint(1,10)  # create test object with random int between 1 & 10
test_obj = sm(integer)


def test_constructor_positive():  # positive test on sm class constructor
    assert test_obj.number == integer


def test_constructor_boolean():
    with raises(TypeError):  # if TypeError is raised, the test passes
        test_obj = sm(True)


def test_constructor_string():
    with raises(TypeError):  # if TypeError is raised, the test passes
        test_obj = sm("teststring")


def test_constructor_float():
    with raises(TypeError):  # if TypeError is raised, the test passes
        test_obj = sm(random.random(1, 10))  # random float between 1 and 10


def test_square_positive():  # positive test on square method
    test_obj_square = test_obj.square()
    assert(test_obj_square == math.pow(integer, 2))


def test_factorial_positive():  # positive test on factorial method
    test_obj_fact = test_obj.factorial()
    assert(test_obj_fact == math.factorial(integer))


def test_power_positive():  # positive test on power method
    test_power = random.randint(2, 5)
    test_obj_power = test_obj.power(test_power)
    assert(test_obj_power == math.pow(integer, test_power))


def test_odd_even_positive():  # positive test on positive method
    test_obj_odd_even = test_obj.odd_or_even()
    odd_even_str = ""
    if (integer % 2) == 0:
        odd_even_str = 'Even'
    if (integer % 2) == 1:
        odd_even_str = "Odd"
    assert (test_obj_odd_even == odd_even_str)


def test_square_root():  # positive test on square root method
    test_obj_sqrt = test_obj.square_root()
    assert (test_obj_sqrt == math.sqrt(integer))
