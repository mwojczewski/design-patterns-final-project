from ingredients.milk.abstract.milk import Milk


class FrothedMilk(Milk):

    def __init__(self, amount: float = 0.0) -> None:
        if not isinstance(amount, float):
            raise TypeError("Non float value")
        if amount < 0:
            raise ValueError("Cannot pass negative value!")
        super().__init__(amount)

    def __str__(self) -> str:
        return f'Frothed Milk'
