from recipes.abstract.recipe import Recipe

from ingredients.coffee_bean.roasted_coffee import RoastedCoffee
from ingredients.milk.regular_milk import RegularMilk
from ingredients.milk.frothed_milk import FrothedMilk

from ingredients.coffee.espresso import Espresso

from components.cup import Cup
from components.grinder import Grinder
from components.infuser import Infuser
from components.frother import Frother


class Cappuccino(Recipe):

    def __init__(self) -> None:
        self.__cup = Cup(200)

    def __str__(self) -> str:
        return f'Cappuccino'

    def add_base_component(self) -> None:
        milk = Frother(RegularMilk(180.0)).pass_milk(FrothedMilk())
        self.__cup.add_ingredient(milk)

    def add_second_component(self) -> None:
        grounded_coffee = Grinder(RoastedCoffee(10.0)).grind()
        infuser = Infuser(grounded_coffee).make_coffee(Espresso, 20.0)
        self.__cup.add_ingredient(infuser)

    def add_top_component(self) -> None:
        pass

    def get_cup(self) -> Cup:
        return self.__cup

    def get_size(self) -> int:
        return self.__cup.get_size()
