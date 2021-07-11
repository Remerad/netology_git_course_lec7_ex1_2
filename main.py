
class CookBook:
    def __init__(self):
        self.cook_book = {}

    def read_cook_book_file(self):
        temp_dish_title = ""
        temp_dish_components = []
        with open('recipes.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if line != "\n":
                    temp_list = f.readline().strip().split(" | ")
                    #print(temp_list)
                    if len(temp_list) == 1:
                        if temp_list[0].isdigit():
                            continue
                        temp_dish_title = temp_list[0]
                        #print(temp_dish_title)
                    else:
                        temp_dish_components.append({'ingredient_name': temp_list[0],
                                                'quantity': temp_list[1], 'measure': temp_list[2]})
                else:
                    print("Хоба!")
                    print(temp_list)
                    print(temp_dish_components)
                    self.cook_book.update({temp_dish_title: temp_dish_components})


if __name__ == '__main__':
    CB = CookBook()
    CB.read_cook_book_file()
    #print(CB.cook_book)
    for i in CB.cook_book:
        #print(CB.cook_book[i])
        print(i)
        for j in CB.cook_book[i]:
            print(j)

