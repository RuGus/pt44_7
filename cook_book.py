class CookBook:
    def __init__(self, file="recipes.txt"):
        self.dishes = {}
        with open(file) as cb_file:
            for line in cb_file:
                dish = line.strip()
                ingredients_count = int(cb_file.readline())
                ingredients_list = []
                for count in range(ingredients_count):
                    ingredient_name, quantity, measure = (
                        cb_file.readline().strip().split(" | ")
                    )
                    ingredients_list.append(
                        {
                            "ingredient_name": ingredient_name,
                            "quantity": quantity,
                            "measure": measure,
                        }
                    )
                self.dishes[dish] = ingredients_list
                cb_file.readline()

    def get_shop_list_by_dishes(self, dishes: list, person_count: int) -> dict:
        if not isinstance(dishes, (list, tuple)):
            raise ValueError("Incorrect argument type")
        else:
            ingredients_shop_list = {}
            for dish in dishes:
                if dish not in self.dishes:
                    print(
                        f"Блюдо '{dish}' отсутствует в кулинарной книге. Исключено из расчета."
                    )
                    continue
                for ingredient in self.dishes[dish]:
                    if ingredient["ingredient_name"] in ingredients_shop_list:
                        ingredients_shop_list[ingredient["ingredient_name"]][
                            "quantity"
                        ] += (int(ingredient["quantity"]) * person_count)
                    else:
                        ingredients_shop_list[ingredient["ingredient_name"]] = {
                            "quantity": int(ingredient["quantity"]) * person_count,
                            "measure": ingredient["measure"],
                        }
            return ingredients_shop_list
