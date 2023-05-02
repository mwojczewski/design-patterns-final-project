from ingredients.coffee_bean.grounded_coffee import GroundedCoffee
from ingredients.abstract.ingredient import Ingredient

from helpers.progressbar import Progressbar
import time
import math


class Infuser:
    flow: float = 10.0  # 10ml / s

    def __init__(self, grounded_coffee: GroundedCoffee) -> None:
        if not isinstance(grounded_coffee, GroundedCoffee):
            raise TypeError("Wrong variant of Grounded Coffee passed!")

        self.grounded_coffee = grounded_coffee

    def __str__(self) -> str:
        return f'Infuser'

    def make_coffee(self, product, water_amount: float) -> Ingredient:
        if not isinstance(product(1.0), Ingredient):
            raise TypeError("Wrong variant of resulting product passed!")
        if not isinstance(water_amount, float):
            raise TypeError("Water must be float! :P")
        if water_amount < 1:
            raise ValueError("Must add water!")

        steps = math.ceil(water_amount / self.flow)
        p = Progressbar(f"Making {product(1.0)}", 0, steps)
        p.draw()
        for i in range(steps):
            time.sleep(1)
            p.increase_step()
            p.draw()

        time.sleep(2)

        return product(water_amount)
