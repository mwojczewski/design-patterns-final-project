# test_with_pytest.py
import pytest

from ingredients.coffee.coffee import Coffee
from ingredients.coffee.espresso import Espresso


def test_ingredients_coffee_proper_initialization():
    assert Coffee(200.0).get_amount() == 200.0
    assert Coffee(1.0).get_amount() == 1.0
    assert Coffee(34342.0).get_amount() == 34342.0
    assert Coffee(9999999.0).get_amount() == 9999999.0
    assert Coffee(432.44444).get_amount() == 432.44444
    assert Coffee(3.141592).get_amount() == 3.141592


def test_ingredients_coffee_improper_initialization():
    with pytest.raises(TypeError):
        Coffee(1)

    with pytest.raises(TypeError):
        Coffee(True)

    with pytest.raises(ValueError):
        Coffee(-1.0)

    with pytest.raises(ValueError):
        Coffee(-154353453.432)

    with pytest.raises(TypeError):
        Coffee("fdkfdsfsd")

    with pytest.raises(TypeError):
        Coffee(Espresso(1.0))


def test_ingredients_espresso_proper_initialization():
    assert Espresso(200.0).get_amount() == 200.0
    assert Espresso(1.0).get_amount() == 1.0
    assert Espresso(34342.0).get_amount() == 34342.0
    assert Espresso(9999999.0).get_amount() == 9999999.0
    assert Espresso(432.44444).get_amount() == 432.44444
    assert Espresso(3.141592).get_amount() == 3.141592


def test_ingredients_espresso_improper_initialization():
    with pytest.raises(TypeError):
        Espresso(1)

    with pytest.raises(TypeError):
        Espresso(True)

    with pytest.raises(ValueError):
        Espresso(-1.0)

    with pytest.raises(ValueError):
        Espresso(-154353453.432)

    with pytest.raises(TypeError):
        Espresso("fdkfdsfsd")

    with pytest.raises(TypeError):
        Espresso(Coffee(1.0))
