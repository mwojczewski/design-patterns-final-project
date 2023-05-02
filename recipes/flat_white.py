from recipes.abstract.recipe import Recipe

from ingredients.coffee_bean.roasted_coffee import RoastedCoffee
from ingredients.milk.regular_milk import RegularMilk
from ingredients.milk.frothed_milk import FrothedMilk

from ingredients.coffee.espresso import Espresso

from components.cup import Cup
from components.grinder import Grinder
from components.infuser import Infuser
from components.frother import Frother


class FlatWhite(Recipe):

    def __init__(self) -> None:
        self.__cup = Cup(200)

    def __str__(self) -> str:
        return f'Flat White'

    def add_base_component(self) -> None:
        grounded_coffee = Grinder(RoastedCoffee(13.0)).grind()
        infuser = Infuser(grounded_coffee).make_coffee(Espresso, 80.0)
        self.__cup.add_ingredient(infuser)

    def add_second_component(self) -> None:
        milk = Frother(RegularMilk(20.0)).pass_milk(RegularMilk())
        self.__cup.add_ingredient(milk)

    def add_top_component(self) -> None:
        milk = Frother(RegularMilk(100.0)).pass_milk(FrothedMilk())
        self.__cup.add_ingredient(milk)

    def get_cup(self) -> Cup:
        return self.__cup

    def get_size(self) -> int:
        return self.__cup.get_size()
