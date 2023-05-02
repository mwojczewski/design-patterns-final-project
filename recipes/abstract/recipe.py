from abc import ABC, abstractmethod
from components.cup import Cup


class Recipe(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        return f'Recipe'

    @abstractmethod
    def add_base_component(self) -> None:
        pass

    @abstractmethod
    def add_second_component(self) -> None:
        pass

    @abstractmethod
    def add_top_component(self) -> None:
        pass

    @abstractmethod
    def get_cup(self) -> Cup:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass
