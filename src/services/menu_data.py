import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu_file(source_path)

    def load_menu_file(self, source_path: str):
        with open(source_path, mode='r', encoding='utf-8') as file:
            menu_dish = None
            file_reader = csv.DictReader(file)

            for line in file_reader:
                ingredient_name = line['ingredient']
                price = float(line['price'])
                name = line['dish']
                recipe_amount = int(line['recipe_amount'])

                for dish in self.dishes:
                    if dish.price == price and dish.name == name:
                        menu_dish = dish
                        break
                else:
                    menu_dish = Dish(name, price)
                    self.dishes.add(menu_dish)

                menu_dish.add_ingredient_dependency(
                    Ingredient(ingredient_name), recipe_amount
                )
