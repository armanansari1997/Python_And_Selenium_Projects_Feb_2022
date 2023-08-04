import sys


class Employee:
    def __init__(self, id, name, job_title, pay_rate):
        self.id = id
        self.name = name
        self.job_title = job_title
        self.pay_rate = pay_rate

    def __str__(self):
        return "[{}, {}, {}, {}]".format(self.id, self.name, self.job_title, self.pay_rate)


def display_menu():
    USER_MENU = {
        "a": "Add Employee",
        "d": "Delete Employee",
        "s": "Search Employee",
        "l": "List all employees",
        "q": "Quit"
    }

    for k, v in USER_MENU.items():
        print("{} - {}".format(k, v))


if __name__ == '__main__':
    display_menu()

    employee_list = []

    user_input = input("Enter your choice ")
    while user_input != 'q':
        if user_input == "a":
            id = eval(input("Enter id "))
            name = input("Enter name ")
            job_title = input("Enter job title ")
            pay_rate = input("Enter pay rate ")
            e = Employee(id, name, job_title, pay_rate)
            employee_list.append(e)
        elif user_input == "d":
            if len(employee_list) > 0:
                del employee_list[0]
                print("One item deleted Successfully")
            else:
                print("Employee list is empty")
        elif user_input == "l":
            for employee in employee_list:
                print(employee)
        elif user_input == "q":
            sys.exit()
        elif user_input == "s":
            search = input("Enter a name which you want to search in the list ")
            for employee in employee_list:
                if search == employee.name:
                    print("Employee is Exist")
                else:
                    print("Employee doesn't Exist")
        else:
            print("Wrong Choice")
            display_menu()
            print("Please choose from above options")
        user_input = input("Enter your choice ")
