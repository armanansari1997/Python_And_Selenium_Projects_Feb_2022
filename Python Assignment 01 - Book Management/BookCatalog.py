import sys


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.read = False

    def __str__(self):
        return "{},{},{}".format(self.name, self.author, self.read)


def display_menu():
    USER_MENU = {
        "a": "Add a new Book",
        "d": "Delete a Book",
        "r": "Mark the Book as Read",
        "l": "List all Books",
        "q": "Quit"
    }

    for k, v in USER_MENU.items():
        print("{} - {}".format(k, v))


if __name__ == '__main__':
    display_menu()

    book_list = []

    user_input = input("Enter Your Choice ")
    while user_input != 'q':
        if user_input == 'a':
            book_name = input("Enter Book Name ")
            author_name = input("Enter Author Name ")
            book = Book(book_name, author_name)
            book_list.append(book)
        elif user_input == 'l':
            print("Books List")
            for book in book_list:
                print(book)
        elif user_input == 'r':
            user_book = input("Enter book name which you want to read")
            for book in book_list:
                if book.name == user_book:
                    book.read = True
                    break
        elif user_input == 'd':
            del_book = input("Enter book name which you want to Delete")
            for book in book_list:
                if book.name == del_book:
                    book_list.remove(book)
        elif user_input == 'q':
            sys.exit()
        else:
            print("Wrong Choice ")
            display_menu()
        user_input = input("Enter your Choice ")
