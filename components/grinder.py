from ingredients.coffee_bean.roasted_coffee import RoastedCoffee
from ingredients.coffee_bean.grounded_coffee import GroundedCoffee
from helpers.progressbar import Progressbar
import time
import math


class Grinder:

    max_beans: float = 60.0

    efficiency: float = 1.3  # g/s

    def __init__(self, roasted_coffee: RoastedCoffee) -> None:
        if not isinstance(roasted_coffee, RoastedCoffee):
            raise TypeError("Wrong variant of coffee passed!")
        self.roasted_coffee = roasted_coffee

    def grind(self) -> GroundedCoffee:
        if not 1 < self.roasted_coffee.get_amount() <= self.max_beans:
            raise ValueError(f"Amount of coffee beans out of range!")

        grounded_coffee = GroundedCoffee(self.roasted_coffee.get_amount())

        steps = math.ceil(self.roasted_coffee.get_amount() / self.efficiency)
        p = Progressbar("Grinding coffee beans", 0, steps)
        p.draw()

        for i in range(steps):
            time.sleep(1)
            p.increase_step()
            p.draw()

        time.sleep(2)

        return grounded_coffee
