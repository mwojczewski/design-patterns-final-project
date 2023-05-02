# test_with_pytest.py
import pytest

from recipes.black_coffee_xl import BlackCoffeeXL
from recipes.coffee_with_milk_xl import CoffeeWithMilkXL
from recipes.flat_white_xl import FlatWhiteXL
from recipes.cafe_latte_xl import CafeLatteXL
from recipes.cappuccino_xl import CappuccinoXL
from recipes.espresso_shot_xl import EspressoShotXL

from ingredients.coffee.coffee import Coffee
from ingredients.milk.abstract.milk import Milk
from ingredients.coffee.espresso import Espresso

from builder import Builder


def test_recipes_black_coffee():
    cup = Builder(BlackCoffeeXL()).build()
    content = cup.get_content()
    assert len(content) == 1
    assert isinstance(content[0], Coffee)


def test_recipes_cafe_latte():
    cup = Builder(CafeLatteXL()).build()
    content = cup.get_content()
    assert len(content) == 3
    assert isinstance(content[0], Milk)
    assert isinstance(content[1], Milk)
    assert isinstance(content[2], Espresso)


def test_recipe_cappuccino():
    cup = Builder(CappuccinoXL()).build()
    content = cup.get_content()
    assert len(content) == 2
    assert isinstance(content[0], Milk)
    assert isinstance(content[1], Espresso)


def test_recipe_coffee_with_milk():
    cup = Builder(CoffeeWithMilkXL()).build()
    content = cup.get_content()
    assert len(content) == 2
    assert isinstance(content[0], Espresso)
    assert isinstance(content[1], Milk)


def test_recipe_espresso_shot():
    cup = Builder(EspressoShotXL()).build()
    content = cup.get_content()
    assert len(content) == 1
    assert isinstance(content[0], Espresso)


def test_recipe_flat_white():
    cup = Builder(FlatWhiteXL()).build()
    content = cup.get_content()
    assert len(content) == 3
    assert isinstance(content[0], Espresso)
    assert isinstance(content[1], Milk)
    assert isinstance(content[2], Milk)
