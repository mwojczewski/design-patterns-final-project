# test_with_pytest.py
import pytest

from recipes.black_coffee import BlackCoffee
from recipes.coffee_with_milk import CoffeeWithMilk
from recipes.flat_white import FlatWhite
from recipes.cafe_latte import CafeLatte
from recipes.cappuccino import Cappuccino
from recipes.espresso_shot import EspressoShot

from ingredients.coffee.coffee import Coffee
from ingredients.milk.abstract.milk import Milk
from ingredients.coffee.espresso import Espresso

from builder import Builder


def test_recipes_black_coffee():
    cup = Builder(BlackCoffee()).build()
    content = cup.get_content()
    assert len(content) == 1
    assert isinstance(content[0], Coffee)


def test_recipes_cafe_latte():
    cup = Builder(CafeLatte()).build()
    content = cup.get_content()
    assert len(content) == 3
    assert isinstance(content[0], Milk)
    assert isinstance(content[1], Milk)
    assert isinstance(content[2], Espresso)


def test_recipe_cappuccino():
    cup = Builder(Cappuccino()).build()
    content = cup.get_content()
    assert len(content) == 2
    assert isinstance(content[0], Milk)
    assert isinstance(content[1], Espresso)


def test_recipe_coffee_with_milk():
    cup = Builder(CoffeeWithMilk()).build()
    content = cup.get_content()
    assert len(content) == 2
    assert isinstance(content[0], Espresso)
    assert isinstance(content[1], Milk)


def test_recipe_espresso_shot():
    cup = Builder(EspressoShot()).build()
    content = cup.get_content()
    assert len(content) == 1
    assert isinstance(content[0], Espresso)


def test_recipe_flat_white():
    cup = Builder(FlatWhite()).build()
    content = cup.get_content()
    assert len(content) == 3
    assert isinstance(content[0], Espresso)
    assert isinstance(content[1], Milk)
    assert isinstance(content[2], Milk)
