
from pytest import raises
import yaml
from ..laboratory import Laboratory
import os

with open(os.path.join(os.path.dirname(__file__),'fixtures.yaml')) as file:
    fixtures=yaml.load(file)

def test_number_of_shelves():
    with raises(TypeError) as exception: 
        Laboratory(fixtures['not_2_shelves'])

def test_random_selection():
    answer1 = fixtures['random_order'].pop('answer1')
    answer2 = fixtures['random_order'].pop('answer2')
    answer3 = fixtures['random_order'].pop('answer3')
    assert Laboratory(fixtures['random_order']) == answer1 or answer2 or answer3

def test_not_numbers():
    with raises(ValueError) as exception: 
        Laboratory(fixtures['not_numbers'])
