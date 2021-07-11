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
                    # print(temp_list)
                    # print(len(temp_dish_components))
                    if len(temp_list) == 1 and temp_list[0] != '':
                        temp_dish_name = temp_list[0]
                        temp_dish_components = []
                        # print(temp_dish_name)
                    elif len(temp_list) > 1:
                        temp_dish_components.append({'ingredient_name': temp_list[0],
                                                     'quantity': int(temp_list[1]),
                                                     'measure': temp_list[2]})
                    elif len(temp_list) == 1 and temp_list[0] == '':
                        # print("Новое блюдо!")
                        self.cook_book.update({temp_dish_name: temp_dish_components})
            # print("Новое блюдо!")
            self.cook_book.update({temp_dish_name: temp_dish_components})

    def get_shop_list_by_dishes(self, dishes, person_count):
        dishes_components_list = {}
        for dish in dishes:
            if dish in self.cook_book:
                print(f"{dish} - знакомое блюдо")
                for component in self.cook_book[dish]:
                    # print(f"{component['ingredient_name']}  ")
                    if component['ingredient_name'] not in dishes_components_list:
                        # print(component['ingredient_name'])
                        # print(component['measure'])
                        # print(component['quantity'])
                        dishes_components_list.update({component['ingredient_name']:
                                                           {'measure': component['measure'],
                                                            'quantity': component['quantity'] * person_count}})
                        # print(dishes_components_list)
                    else:
                        # print("Совпадение")
                        # print(dishes_components_list.get(component['ingredient_name']))
                        q = dishes_components_list.get(component['ingredient_name'])['quantity'] \
                            + component['quantity'] * person_count
                        dishes_components_list.update({component['ingredient_name']:
                                                           {'measure': component['measure'],
                                                            'quantity': q}})
        #print(dishes_components_list)
        return dishes_components_list


if __name__ == '__main__':
    CB = CookBook()
    CB.read_cook_book_file()
    #for i in CB.cook_book:
    #    print(CB.cook_book[i])
    #    print(i)
    #    for j in CB.cook_book[i]:
    #        print(j)

    shop_list = CB.get_shop_list_by_dishes(["Омлет", "Фахитос"], 4)
    for i in shop_list:
        print(f"{i}, {shop_list[i]['quantity']} {shop_list[i]['measure']}")