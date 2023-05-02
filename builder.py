from recipes.abstract.recipe import Recipe
from components.cup import Cup


class Builder:

    def __init__(self, recipe: Recipe) -> None:
        self.__recipe = recipe

    def __str__(self):
        return f'Builder'

    def build(self) -> Cup:
        try:
            self.__recipe.add_base_component()
            self.__recipe.add_second_component()
            self.__recipe.add_top_component()
            cup = self.__recipe.get_cup()
            return cup
        except ValueError:
            print("An ValueError occurred!")
        except TypeError:
            print("TypeError occurred!")

    def get_recipe(self) -> Recipe:
        return self.__recipe