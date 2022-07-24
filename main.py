def get_recipes_from_files(file_name):
    """
    метод возвращает словарь со списком ингридиентов для блюда
    in:
    file_name - имя файла с рецептами
    out:
    cook_book - словарь со списком ингридиентов для блюда
    """
    cook_book = {}
    with open(file_name, 'r') as f:
        dish = ''
        for line in f:
            line = line.replace('\n', '')
            digit = line.isdigit()
            # не содержит символ |, не число и не пустая строка
            the_name_of_the_dish = '|' not in line and not digit and line != ''
            # не число и содержит символ |
            ingredients = not digit and '|' in line
            if the_name_of_the_dish:
                dish = line
                cook_book[dish] = []
            elif ingredients:
                ingredient_name, quantity, measure = line.split('|')
                cook_book[dish].append({'ingredient_name': ingredient_name,
                                        'quantity': quantity,
                                        'measure': measure})
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """
    метод возвращает список ингридиентов для приготовления блюда с учётом кол-ва персон
    in:
    dishes - список блюд
    person_count - кол-во персон
    cook_book - словарь со списком ингридиентов
    out:
    shop_list_by_dishes - словарь с названием ингредиентов и его количества для блюда
    """
    shop_list_by_dishes = {}
    for dish in dishes:
        ingredient_list = cook_book[dish]
        for ingredient in ingredient_list:
            name = ingredient['ingredient_name']
            qty = int(ingredient['quantity']) * person_count
            if name not in shop_list_by_dishes:
                shop_list_by_dishes[name] = qty
            else:
                shop_list_by_dishes[name] += qty
    return shop_list_by_dishes


def merge_files(files):
    """
    метод записывает файл в нужном виде(объединяя 3 файла и внося служебную информацию)
    in:
    files - список файлов которые нужно объединить
    out:
    записывает файл в нужном виде(объединяя 3 файла и внося служебную информацию)
    """
    output = {}
    for file_name in files:
        content = open(file_name).read().split('\n')
        service_information = file_name + '\n' + str(len(content)) + '\n'
        content.insert(0, service_information)
        content.append('\n')
        output[len(content)] = content
    output_file = [output[i] for i in sorted(output)]
    with open('output_file.txt', 'w') as f:
        [f.write(i1) for i in output_file for i1 in i]


def main():
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, get_recipes_from_files('recipes.txt'))
    merge_files(['1.txt', '2.txt', '3.txt'])


if __name__ == "__main__":
    main()
