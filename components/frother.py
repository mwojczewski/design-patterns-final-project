from ingredients.milk.abstract.milk import Milk
from ingredients.milk.regular_milk import RegularMilk
from helpers.progressbar import Progressbar
import time
import math


class Frother:
    flow: float = 15.0  # ml/s

    def __init__(self, standard_milk: RegularMilk) -> None:
        if not isinstance(standard_milk, RegularMilk):
            raise TypeError("Wrong variant of milk passed!")
        self.standard_milk = standard_milk


    def __str__(self) -> str:
        return f'Frother'

    def __process_milk(self, amount: float = 0.0, name: str = "") -> None:
        steps = math.ceil(amount / self.flow)
        p = Progressbar(name, 0, steps)
        p.draw()

        for i in range(steps):
            time.sleep(1)
            p.increase_step()
            p.draw()

        time.sleep(2)

    def pass_milk(self, variant: Milk) -> Milk:
        if not isinstance(variant, Milk):
            raise TypeError("Variant of Milk expected!")

        output_milk = variant
        self.__process_milk(self.standard_milk.get_amount(), f'Adding {variant}')

        output_milk.add(self.standard_milk.get_amount())
        self.standard_milk.subtract(self.standard_milk.get_amount())

        return output_milk
