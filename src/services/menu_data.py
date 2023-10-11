import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.menu_file(source_path)

    def menu_file(self, source_path: str):
        with open(source_path, mode='r', encoding='utf-8') as file:
            file_reader = csv.DictReader(file)
            menu_dish = None

            for line in file_reader:
                price = float(line['price'])
                name = line['dish']
                ingredient_name = line['ingredient']
                amount = int(line['amount'])

                for dish in self.dishes:
                    if dish.price == price and dish.name == name:
                        menu_dish = dish
                        break
                    else:
                        menu_dish = Dish(name, price)
                        self.dishes.add(menu_dish)

                ingredient = Ingredient(ingredient_name)
                menu_dish.add_ingredient_dependency(ingredient, amount)
