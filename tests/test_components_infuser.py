# test_with_pytest.py
import pytest

from components.infuser import *
from ingredients.coffee_bean.grounded_coffee import GroundedCoffee
from ingredients.coffee_bean.roasted_coffee import RoastedCoffee
from ingredients.coffee.coffee import Coffee
from ingredients.coffee.espresso import Espresso


def test_infuser_proper_initialization():
    assert Infuser(GroundedCoffee(200.0))
    assert Infuser(GroundedCoffee(1.0))
    assert Infuser(GroundedCoffee(4340.0))
    assert Infuser(GroundedCoffee(500.0))
    assert Infuser(GroundedCoffee(54253424235245.0))
    assert Infuser(GroundedCoffee(12.0))


def test_infuser_improper_initialization():
    with pytest.raises(TypeError):
        Infuser(RoastedCoffee(200.0))
        Infuser(RoastedCoffee(200))
        Infuser(RoastedCoffee(-331))
        Infuser(RoastedCoffee(-331.0))
        Infuser(RoastedCoffee("fjsdfjdsfjhsdklfs"))

    with pytest.raises(ValueError):
        Infuser(RoastedCoffee(-200.0))
        Infuser(RoastedCoffee(0.0))
        Infuser(RoastedCoffee(0))
        Infuser(RoastedCoffee(4234545434242))
        Infuser(RoastedCoffee("rewfouhdsihfsk"))


def test_infuser_make_proper_espresso():
    assert isinstance(Infuser(GroundedCoffee(20.0)).make_coffee(Espresso, 1.0), Ingredient)
    assert isinstance(Infuser(GroundedCoffee(1.0)).make_coffee(Espresso, 10.0), Ingredient)
    assert isinstance(Infuser(GroundedCoffee(3232.0)).make_coffee(Espresso, 100.0), Ingredient)
    assert isinstance(Infuser(GroundedCoffee(1111111111.0)).make_coffee(Espresso, 243.0), Ingredient)
    assert isinstance(Infuser(GroundedCoffee(322.0)).make_coffee(Espresso, 23.0), Ingredient)


def test_infuser_make_proper_coffee():
    assert isinstance(Infuser(GroundedCoffee(20.0)).make_coffee(Coffee, 10.0), Ingredient)
    assert isinstance(Infuser(GroundedCoffee(1.0)).make_coffee(Coffee, 1.0), Ingredient)
    assert isinstance(Infuser(GroundedCoffee(3243.0)).make_coffee(Coffee, 100.0), Ingredient)
    assert isinstance(Infuser(GroundedCoffee(222222222.0)).make_coffee(Coffee, 242.0), Ingredient)
    assert isinstance(Infuser(GroundedCoffee(985.0)).make_coffee(Coffee, 54.0), Ingredient)


def test_infuser_make_improper_coffee_type():
    with pytest.raises(TypeError):
        Infuser(GroundedCoffee(20.0)).make_coffee(GroundedCoffee, 20.0)

    with pytest.raises(TypeError):
        Infuser(GroundedCoffee(20.0)).make_coffee(Coffee, 4)

    with pytest.raises(TypeError):
        Infuser(GroundedCoffee(20.0)).make_coffee(Coffee, -4)

    with pytest.raises(TypeError):
        Infuser(GroundedCoffee(20.0)).make_coffee(Coffee, -434324324)

    with pytest.raises(TypeError):
        Infuser(GroundedCoffee(20.0)).make_coffee(Coffee, 44325453543433)

    with pytest.raises(ValueError):
        Infuser(GroundedCoffee(20.0)).make_coffee(Coffee, -4.0)

    with pytest.raises(ValueError):
        Infuser(GroundedCoffee(20.0)).make_coffee(Coffee, 0.0)

    with pytest.raises(ValueError):
        Infuser(GroundedCoffee(20.0)).make_coffee(Coffee, 0.5)

    with pytest.raises(ValueError):
        Infuser(GroundedCoffee(20.0)).make_coffee(Coffee, -434324324.0)

    with pytest.raises(ValueError):
        Infuser(GroundedCoffee(20.0)).make_coffee(Coffee, 0.9999)
