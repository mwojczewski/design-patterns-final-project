from ingredients.abstract.ingredient import Ingredient


class Espresso(Ingredient):

    def __init__(self, amount: float = 0.0) -> None:
        if not isinstance(amount, float):
            raise TypeError("Non float value")
        if amount < 1:
            raise ValueError("Cannot add 0ml or less!")
        super().__init__(amount)

    def __str__(self) -> str:
        return f'Espresso'

    def get_amount(self) -> float:
        return super().get_amount()
