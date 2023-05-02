from ingredients.abstract.ingredient import Ingredient


class Milk(Ingredient):

    def __init__(self, amount: float = 0.0) -> None:
        super().__init__(amount)

    def __str__(self) -> str:
        return 'Milk'

    def add(self, amount: float = 0.0) -> None:
        self.increase(amount)

    def subtract(self, amount: float = 0.0) -> None:
        self.decrease(amount)

    def get_amount(self) -> float:
        return super().get_amount()
