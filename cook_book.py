class CookBook:
    def __init__(self, file='recipes.txt'):
        self.dishes = {}
        with open(file) as cb_file:
            for line in cb_file:
                dish = line.strip()
                ingredients_count = int(cb_file.readline())
                ingredients_list = []
                for count in range(ingredients_count):
                    ingredient_name, quantity, measure = cb_file.readline().strip().split(' | ')
                    ingredients_list.append(
                        {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
                self.dishes[dish] = ingredients_list
                cb_file.readline()
