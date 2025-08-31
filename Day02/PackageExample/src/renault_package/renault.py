
gname = "Rohit Sharma"

sports = ['cricket', 'hockey', 'boxing', 'tennis', 'swimming']

runs = {'odi': 12500, 'test': 850, 't20': 2800}

def greet(gnm):
    print(f"Greetings Mr.{gnm}, Welcome to the event.....")

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

# print("Module Name :", __name__)

# implementation
if __name__ == '__main__':
    greet("Ravi")

    emp1 = Employee("Jack", 8500)
    print(emp1)
