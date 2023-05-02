# test_with_pytest.py
import pytest

from components.frother import *
from ingredients.milk.regular_milk import RegularMilk
from ingredients.milk.frothed_milk import FrothedMilk
from ingredients.coffee.espresso import Espresso


def test_frother_proper_material_initialization():
    assert Frother(RegularMilk(200.0))
    assert Frother(RegularMilk(2.0))
    assert Frother(RegularMilk(8000.0))
    assert Frother(RegularMilk(323.0))
    assert Frother(RegularMilk(123443432423.0))


def test_frother_passing_improper_ingredient_amount():
    with pytest.raises(TypeError):
        Frother(RegularMilk(200))

    with pytest.raises(TypeError):
        Frother(RegularMilk(20043243242))

    with pytest.raises(TypeError):
        Frother(RegularMilk(-32120043243242))

    with pytest.raises(TypeError):
        Frother(RegularMilk('dasdasdad'))


def test_frother_improper_material_initialization():
    with pytest.raises(TypeError):
        Frother(FrothedMilk(200.0))


def test_frother_passing_frothed_milk():
    assert isinstance(Frother(RegularMilk(200.0)).pass_milk(FrothedMilk()), FrothedMilk)


def test_frother_passing_regular_milk():
    assert isinstance(Frother(RegularMilk(200.0)).pass_milk(RegularMilk()), RegularMilk)


def test_frother_passing_invalid_expected_milk_type():
    with pytest.raises(TypeError):
        Frother(RegularMilk(200.0)).pass_milk(Espresso(1.0))
