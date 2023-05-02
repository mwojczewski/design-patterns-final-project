import sys

from builder import Builder
from recipes.black_coffee import BlackCoffee
from recipes.black_coffee_xl import BlackCoffeeXL
from recipes.cafe_latte import CafeLatte
from recipes.cafe_latte_xl import CafeLatteXL
from recipes.cappuccino import Cappuccino
from recipes.cappuccino_xl import CappuccinoXL
from recipes.coffee_with_milk import CoffeeWithMilk
from recipes.coffee_with_milk_xl import CoffeeWithMilkXL
from recipes.espresso_shot import EspressoShot
from recipes.espresso_shot_xl import EspressoShotXL
from recipes.flat_white import FlatWhite
from recipes.flat_white_xl import FlatWhiteXL
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_recipe(builders):
    try:
        option = input("[e]spresso, c[a]ppuccino, [b]lack coffee, [c]offee with milk, [l]atte, [f]lat white or e[x]it ? ")
        builder = builders[option]()

    except KeyError:
        if option == "x":
            print("Bye!")
            exit(1)

        print('Sorry, that option is not available. Choose one from listed below:')
        return False, None

    return True, builder


def main():
    while 1:
        cls()
        builders = dict(e=EspressoShot, E=EspressoShotXL,
                        a=Cappuccino, A=CappuccinoXL,
                        b=BlackCoffee, B=BlackCoffeeXL,
                        c=CoffeeWithMilk, C=CoffeeWithMilkXL,
                        l=CafeLatte, L=CafeLatteXL,
                        f=FlatWhite, F=FlatWhiteXL)
        print("Welcome to my Coffee Machine!\n")
        print("Choose your favourite drink (use capital letter for bigger size):")

        valid_input = False
        while not valid_input:
            valid_input, selected_builder = validate_recipe(builders)

        builder = Builder(selected_builder)
        cls()
        print(f'Making {str(builder.get_recipe())} in {builder.get_recipe().get_size()}ml cup\n')
        cup = builder.build()
        cup.describe_content()

        print("Press ENTER to go back to main menu.")
        sys.stdin.readline()


if __name__ == '__main__':
    main()
