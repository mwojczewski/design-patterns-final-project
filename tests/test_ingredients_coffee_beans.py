# test_with_pytest.py
import pytest

from ingredients.coffee_bean.grounded_coffee import GroundedCoffee
from ingredients.coffee_bean.roasted_coffee import RoastedCoffee


def test_ingredients_roasted_coffee_proper_initialization():
    assert RoastedCoffee(200.0).get_amount() == 200.0
    assert RoastedCoffee(1.0).get_amount() == 1.0
    assert RoastedCoffee(34342.0).get_amount() == 34342.0
    assert RoastedCoffee(9999999.0).get_amount() == 9999999.0
    assert RoastedCoffee(432.44444).get_amount() == 432.44444
    assert RoastedCoffee(3.141592).get_amount() == 3.141592


def test_ingredients_roasted_coffee_improper_initialization():
    with pytest.raises(TypeError):
        RoastedCoffee(1)

    with pytest.raises(TypeError):
        RoastedCoffee(True)

    with pytest.raises(ValueError):
        RoastedCoffee(-1.0)

    with pytest.raises(ValueError):
        RoastedCoffee(-154353453.432)

    with pytest.raises(TypeError):
        RoastedCoffee("fdkfdsfsd")

    with pytest.raises(TypeError):
        RoastedCoffee(GroundedCoffee(1.0))


def test_ingredients_grounded_coffee_proper_initialization():
    assert GroundedCoffee(200.0).get_amount() == 200.0
    assert GroundedCoffee(1.0).get_amount() == 1.0
    assert GroundedCoffee(34342.0).get_amount() == 34342.0
    assert GroundedCoffee(9999999.0).get_amount() == 9999999.0
    assert GroundedCoffee(432.44444).get_amount() == 432.44444
    assert GroundedCoffee(3.141592).get_amount() == 3.141592


def test_ingredients_grounded_coffee_improper_initialization():
    with pytest.raises(TypeError):
        GroundedCoffee(1)

    with pytest.raises(TypeError):
        GroundedCoffee(True)

    with pytest.raises(ValueError):
        GroundedCoffee(-1.0)

    with pytest.raises(ValueError):
        GroundedCoffee(-154353453.432)

    with pytest.raises(TypeError):
        GroundedCoffee("fdkfdsfsd")

    with pytest.raises(TypeError):
        GroundedCoffee(RoastedCoffee(1.0))
