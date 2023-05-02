# test_with_pytest.py
import pytest

from ingredients.milk.regular_milk import RegularMilk
from ingredients.milk.frothed_milk import FrothedMilk


def test_regular_milk_proper_initialization():
    assert RegularMilk(1.0).get_amount() == 1.0
    assert RegularMilk(555.432).get_amount() == 555.432
    assert RegularMilk(100.0).get_amount() == 100.0
    assert RegularMilk(43423.35432).get_amount() == 43423.35432

    assert RegularMilk(45453.0).get_amount() == 45453.0


def test_regular_milk_improper_initialization():
    with pytest.raises(TypeError):
        RegularMilk(1)

    with pytest.raises(TypeError):
        RegularMilk(True)

    with pytest.raises(ValueError):
        RegularMilk(-1.0)

    with pytest.raises(ValueError):
        RegularMilk(-154353453.432)

    with pytest.raises(TypeError):
        RegularMilk("fdkfdsfsd")

    with pytest.raises(TypeError):
        RegularMilk(FrothedMilk(1.0))


def test_frothed_milk_proper_initialization():
    assert FrothedMilk(1.0).get_amount() == 1.0
    assert FrothedMilk(555.432).get_amount() == 555.432
    assert FrothedMilk(100.0).get_amount() == 100.0
    assert FrothedMilk(43423.35432).get_amount() == 43423.35432

    assert FrothedMilk(45453.0).get_amount() == 45453.0


def test_frothed_milk_improper_initialization():
    with pytest.raises(TypeError):
        FrothedMilk(1)

    with pytest.raises(TypeError):
        FrothedMilk(-1)

    with pytest.raises(ValueError):
        FrothedMilk(-1.0)

    with pytest.raises(ValueError):
        FrothedMilk(-154353453.432)

    with pytest.raises(TypeError):
        FrothedMilk(True)

    with pytest.raises(TypeError):
        FrothedMilk("fdkfdsfsd")

    with pytest.raises(TypeError):
        FrothedMilk(RegularMilk(1.0))
