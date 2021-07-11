
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
                    #print(temp_list)
                    #print(len(temp_dish_components))
                    if len(temp_list) == 1 and temp_list[0] != '':
                        temp_dish_name = temp_list[0]
                        temp_dish_components = []
                        #print(temp_dish_name)
                    elif len(temp_list) > 1:
                        temp_dish_components.append({'ingredient_name': temp_list[0],
                                                     'quantity': temp_list[1],
                                                     'measure': temp_list[2]})
                    elif len(temp_list) == 1 and temp_list[0] == '':
                        #print("Новое блюдо!")
                        self.cook_book.update({temp_dish_name: temp_dish_components})
            #print("Новое блюдо!")
            self.cook_book.update({temp_dish_name: temp_dish_components})



if __name__ == '__main__':
    CB = CookBook()
    CB.read_cook_book_file()
    for i in CB.cook_book:
        #print(CB.cook_book[i])
        print(i)
        for j in CB.cook_book[i]:
            print(j)


