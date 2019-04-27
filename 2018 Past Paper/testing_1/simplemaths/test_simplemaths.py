from pytest import raises
from simplemaths.simplemaths import SimpleMaths as sm
import numpy as np
import math

## add self in individual function since it's in a class!
class TestSimpleMaths():
    def test_constructor_input_float(self):
        with raises(ValueError) as exception: 
            test=sm(0.1)

    def test_constructor_input_string(self):
        with raises(ValueError) as exception: 
            test=sm('a')

    def test_constructor_input_complex(self):
        with raises(ValueError) as exception: 
            test=sm(2j) 

    def test_constructor_input_boolean(self):
        with raises(ValueError) as exception: 
            test=sm(False) 

    def test_square(self):
        for num in range (5):
            test=sm(num)
            assert test.square() == np.square(num)

    def test_factorial(self):
        test=sm(-4)
        with raises(ValueError) as exception: 
            test.factorial()

        for num in range (5):
            test=sm(num)
            assert test.factorial() == math.factorial(num)

    def test_power(self):
        test=sm(3)
        with raises(ValueError) as exception: 
            test.power(False)

        for num in range (5):
            test=sm(num)
            for x in np.arange(4):
                assert test.power(x) == math.pow(num,x)

    def test_odd_or_even(self):
        for num in np.arange(0,12,2):
            test=sm(num)
            assert test.odd_or_even() == 'Even'

        for num in np.arange(1,11,2):
            test=sm(num)
            assert test.odd_or_even() == 'Odd'

    def test_square_root(self):
        test=sm(-4)
        with raises(ValueError) as exception: 
            test.square_root()

        for num in np.arange (5):
            test=sm(num)
            assert test.square_root() == np.sqrt(num)
   
    pass


