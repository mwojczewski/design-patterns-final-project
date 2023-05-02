# test_with_pytest.py
import pytest

from components.cup import *
from ingredients.milk.regular_milk import RegularMilk
from ingredients.milk.frothed_milk import FrothedMilk
from ingredients.coffee.coffee import Coffee
from ingredients.coffee.espresso import Espresso
from ingredients.coffee_bean.roasted_coffee import RoastedCoffee


def test_too_big_cup_size():
    with pytest.raises(ValueError):
        Cup(5000)
    with pytest.raises(ValueError):
        Cup(505)
    with pytest.raises(ValueError):
        Cup(50500000000000033432432)


def test_too_small_cup_size():
    with pytest.raises(ValueError):
        Cup(0)

    with pytest.raises(ValueError):
        Cup(0.99)

    with pytest.raises(ValueError):
        Cup(0.5)


def test_negative_cup_size():
    with pytest.raises(ValueError):
        Cup(-500)

    with pytest.raises(ValueError):
        Cup(-1)

    with pytest.raises(ValueError):
        Cup(-4324354543353)

def test_wrong_value_cup_size():
    with pytest.raises(TypeError):
        Cup("0000")

    with pytest.raises(TypeError):
        Cup("fasdsadfadsfcsa")

    with pytest.raises(TypeError):
        Cup("-2eeewds")


def test_default_cup_size():
    assert 1 < Cup().get_size() < 500


def test_specified_in_range_cup_size():
    assert Cup(300)
    assert Cup(10)
    assert Cup(499)
    assert Cup(343)
    assert Cup(121)
    assert Cup(60)


def test_add_valid_ingredient():
    cup = Cup(200)
    assert cup.add_ingredient(RegularMilk(200.0)) is None
    assert cup.add_ingredient(FrothedMilk(100.0)) is None
    assert cup.add_ingredient(Coffee(50.0)) is None
    assert cup.add_ingredient(Espresso(1.0)) is None


def test_add_invalid_ingredient():
    with pytest.raises(TypeError):
        Cup(200).add_ingredient(RoastedCoffee(200))
