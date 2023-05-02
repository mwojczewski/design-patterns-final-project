from recipes.abstract.recipe import Recipe

from ingredients.coffee_bean.roasted_coffee import RoastedCoffee
from ingredients.coffee.coffee import Coffee

from components.cup import Cup
from components.grinder import Grinder
from components.infuser import Infuser


class BlackCoffee(Recipe):

    def __init__(self) -> None:
        self.__cup = Cup(200)

    def __str__(self) -> str:
        return f'Black Coffee'

    def add_base_component(self) -> None:
        grounded_coffee = Grinder(RoastedCoffee(12.0)).grind()
        infuser = Infuser(grounded_coffee).make_coffee(Coffee, 200.0)
        self.__cup.add_ingredient(infuser)

    def add_second_component(self) -> None:
        pass

    def add_top_component(self) -> None:
        pass

    def get_cup(self) -> Cup:
        return self.__cup

    def get_size(self) -> int:
        return self.__cup.get_size()
