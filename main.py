from pprint import pprint
cook_book = {}
with open('recipes.txt', encoding = 'utf-8') as f:
    for line in f:
        dish = line.strip()
        count = f.readline()
        recipes = []
        for ingredients in range(int(count)):
            ingredient, quantity, measure = f.readline().strip().split('|')
            recipes.append({'ingredient_name': ingredient, 'quantity': quantity, 'measure': measure})
        cook_book.setdefault(dish, recipes)
        skip = f.readline()

#def get_shop_list_by_dishes(dishes, person_count):

pprint(cook_book)