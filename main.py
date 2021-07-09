
class CookBook:
    def __init__(self):
        self.cook_book = {}

    def read_cook_book_file(self, file_name):
        with open(file_name, 'r') as f:
            print(f.readline)


if __name__ == '__main__':
    CB = CookBook
    CB.read_cook_book_file('recipes.txt')

