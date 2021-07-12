class CookBook:
    def __init__(self):
        self.cook_book = {}

    def read_cook_book_file(self):
        temp_dish_name = ""
        temp_dish_components = []
        with open('recipes.txt', 'r', encoding='utf-8') as f:
            my_lines = list(f)
            for i in my_lines:
                temp_str = i.strip()
                if not temp_str.isdigit():
                    temp_list = temp_str.split(" | ")
                    if len(temp_list) == 1 and temp_list[0] != '':
                        temp_dish_name = temp_list[0]
                        temp_dish_components = []
                    elif len(temp_list) > 1:
                        temp_dish_components.append({'ingredient_name': temp_list[0],
                                                     'quantity': int(temp_list[1]),
                                                     'measure': temp_list[2]})
                    elif len(temp_list) == 1 and temp_list[0] == '':
                        self.cook_book.update({temp_dish_name: temp_dish_components})
            self.cook_book.update({temp_dish_name: temp_dish_components})

    def get_shop_list_by_dishes(self, dishes, person_count):
        dishes_components_list = {}
        for dish in dishes:
            if dish in self.cook_book:
                for component in self.cook_book[dish]:
                    if component['ingredient_name'] not in dishes_components_list:
                        dishes_components_list.update({component['ingredient_name']:
                                                           {'measure': component['measure'],
                                                            'quantity': component['quantity'] * person_count}})
                    else:
                        q = dishes_components_list.get(component['ingredient_name'])['quantity'] \
                            + component['quantity'] * person_count
                        dishes_components_list.update({component['ingredient_name']:
                                                           {'measure': component['measure'],
                                                            'quantity': q}})
        return dishes_components_list


if __name__ == '__main__':
    CB = CookBook()
    CB.read_cook_book_file()

    shop_list = CB.get_shop_list_by_dishes(["Омлет", "Фахитос"], 4)
    for i in shop_list:
        print(f"{i}, {shop_list[i]['quantity']} {shop_list[i]['measure']}")