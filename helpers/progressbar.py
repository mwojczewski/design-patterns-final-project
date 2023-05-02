import math
import sys


class Progressbar:

    def __init__(self, name: str = "", step: int = 0, steps: int = 0) -> None:
        self.__name = name
        self.__step = step
        self.__steps = steps

    def draw(self) -> None:
        # prevent printing when tests are running
        if "pytest" in sys.modules:
            return

        percent = math.ceil(100 * (self.__step / self.__steps))
        bar = '█' * percent + '_' * (100 - percent)
        print(f"|{bar}|{self.__name:25s}|", end="\r")

    def increase_step(self):
        self.__step += 1

    def set_step(self, step: int = 0) -> None:
        self.__step = step

    def get_step(self) -> int:
        return self.__step
