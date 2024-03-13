# class members = attributes(variable)+ actions (mehtods)
# we can these variable using object outside the class 

# syntax 

# accessing attributes =object_name.varaible_name
# accessing method =object_name.method_name


class Employee: 
    def __init__(self,sal,age): 
        self.salary=sal
        self.age=age
    def display(self): 
        print(f"The salary is {self.salary} and the age is{self.age}")

e1=Employee(23000,23)
e2=Employee(24000,24)
print(e1.salary)
print(e2.salary)
print(e1.age)
print(e2.age)
print(e1.display())
print(e2.display())
print(" after update the attribute")

print(e1.salary)
print(e2.salary)
e1.salary=28000
e2.salary=29000

print(e1.__dict__)
print(e2.__dict__)
print(e1.salary)
print(e2.salary)
print("How to access the mehtod in the oops")
# How to accessing the display method 
print(e2.display())
print(e1.display())
