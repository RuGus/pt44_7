import cook_book


cook_book = cook_book.CookBook(file="recipes.txt")

print(cook_book.dishes.keys())
print(cook_book.get_shop_list_by_dishes(["Омлет", "Фахитос", "Лобстер"], 2))
