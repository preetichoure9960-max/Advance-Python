#student.py
class Student:
    
    def __init__(self,name,roll,branch):
        self.name = name
        self.roll = roll
        self.branch = branch

    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Branch:",self.branch)

s1 = Student("Preeti",101,"AI & DS")

s1.display()

#employee.py
class Employee:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:",self.name)
        print("Salary:",self.salary)

e1 = Employee("Rahul",50000)

e1.display()

#bankaccount.py
class BankAccount:
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def display(self):
        print("Name:",self.name)
        print("Balance:",self.balance)

b1 = BankAccount("Preeti",1000)

b1.deposit(500)

b1.display()