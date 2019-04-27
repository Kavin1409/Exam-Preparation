
from pytest import raises
import yaml
from ..laboratory import Laboratory
import os

with open(os.path.join(os.path.dirname(__file__),'fixtures.yaml')) as file:
    fixtures=yaml.load(file)

def test_number_of_shelves():
    with raises(TypeError) as exception: 
        Laboratory(fixtures['not_2_shelves'])