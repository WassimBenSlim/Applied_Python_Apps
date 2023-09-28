
class Employee :
    count = 0 
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count += 1
    def displayCount(self):
        print("There are %d Employees." %Employee.count)
    def displayDetails(self):
        print("Name : ", self.name, ",  Position : ", self.position, ",  Salary :",self.salary)

emp1 = Employee("Aladin","CEO",8500)
emp2 = Employee("Jake","Manager",7000)
emp3 = Employee("Stephen","Developer",2750)
emp4 = Employee("Ahmed","Engineer",4600)
print()
emp4.displayCount()
print()
print("**Employees Details**")
print()
emp1.displayDetails()
emp2.displayDetails()
emp3.displayDetails()
emp4.displayDetails()
print()