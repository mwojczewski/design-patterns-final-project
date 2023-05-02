import pytest

from components.grinder import *

from ingredients.coffee_bean.roasted_coffee import RoastedCoffee
from ingredients.coffee_bean.grounded_coffee import GroundedCoffee


def test_grinder_proper_coffee_initialization():
    assert Grinder(RoastedCoffee(40.0))


def test_grinder_improper_coffee_initialization():
    with pytest.raises(TypeError):
        Grinder(GroundedCoffee(200.0))


def test_grinder_grind_accepted_amount():
    assert (Grinder(RoastedCoffee(10.0)).grind())


def test_grinder_grind_exceeding_amount():
    with pytest.raises(ValueError):
        Grinder(RoastedCoffee(501.0)).grind()

    with pytest.raises(ValueError):
        Grinder(RoastedCoffee(550.0)).grind()

    with pytest.raises(ValueError):
        Grinder(RoastedCoffee(5321321350.0)).grind()


def test_grinder_grind_receding_amount():
    with pytest.raises(ValueError):
        Grinder(RoastedCoffee(0.0)).grind()


def test_grinder_grind_negative_amount():
    with pytest.raises(ValueError):
        Grinder(RoastedCoffee(-2.0)).grind()

    with pytest.raises(ValueError):
        Grinder(RoastedCoffee(-23232.0)).grind()
