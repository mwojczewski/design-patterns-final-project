from ingredients.abstract.ingredient import Ingredient


class Cup:

    def __init__(self, cup_size: int = 200) -> None:
        if not 1 <= cup_size <= 500:
            raise ValueError("Wrong cup size passed!")

        self.__size: int = cup_size # ml
        self.__contains: list = []

    def __str__(self) -> str:
        return f'Cup {self.__size}ml'

    def add_ingredient(self, ingredient: Ingredient) -> None:
        if not isinstance(ingredient, Ingredient):
            raise TypeError("Wrong ingredient class!")
        self.__contains.append(ingredient)

    def describe_content(self) -> None:
        print(f"\n\nContent of {self}:\n")
        total = 0
        for item in self.__contains:
            print(f'* {str(item) +":":<15}{item.get_amount():>5}ml')
            total += item.get_amount()

        print(f'------------------------')
        print(f'{"TOTAL:":>16} {total:>5}ml\n')

    def get_content(self) -> list:
        return self.__contains

    def get_size(self) -> int:
        return self.__size

    def reset(self) -> None:
        self.__contains.clear()
