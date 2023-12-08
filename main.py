with open('recipes.txt', 'r', encoding='utf-8') as f:
    file_as_str = f.read()

file_as_list = file_as_str.split('\n')
result = []
temp = []
for line in file_as_list:
    if line != '':
        temp.append(line)
    else:
        result.append(temp.copy())
        temp.clear()

cook_book = {}
for recipe in result:
    name = recipe[0]
    cook_book[name] = []
    for ingredient in recipe[2:]:
        ing_data = ingredient.split('|')
        cook_book[name].append({'ingredient_name': ing_data[0],
                                'quantity': int(ing_data[1]),
                                'measure': ing_data[2]})

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    res = {}

    for dish in dishes:
        # создаем список ингридиентов для 1 человека
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            if name not in res.keys():
                res[name] = {'quantity': ingredient['quantity'],
                             'measure': ingredient['measure']}
            else:
                res[name]["quantity"] += ingredient['quantity']
            res[name]["quantity"] = res[name]["quantity"] * person_count
    return res


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4))


# Напишем функцию для открытия файла

def read_file(name_file):
    line_count = 0
    list_file = []
    dict_file = {}
    with open(name_file, encoding='utf-8') as f:
        for line_file in f:
            line_count += 1
            list_file.append(line_file)
        value = [name_file] + [line_count] + list_file
        dict_file[line_count] = value
    return dict_file


dict1 = read_file('1.txt')
dict2 = read_file('2.txt')
dict3 = read_file('3.txt')

sum_dict = dict1 | dict2 | dict3
sort_dict = dict(sorted(sum_dict.items()))

with open('result.txt', 'w') as f:
    for key in sort_dict.keys():
        for read in sort_dict[key]:
            f.write((str(read).strip() + '\n'))
