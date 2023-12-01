import time
class Employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    def display(self):
        print(f"name of is {self.name} and the salary{self.salary}")
    def __del__(self):
        print("Destructor is called")
e1=Employee("sahntanu",50000)

e2=e1
del e1
time.sleep(5)
class Employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    def display(self):
        print(f"name is {self.name} and the salary is{self.salary}")
    #defing the destructor
    def __del__(self):
        print("Destroctor is called")

#############################################
#disadvantages of the  Destructor
import time
class Employee:
      def __init__(self,obj2):
          self.obj2=obj2
      def __del_(self):
          print("Employee class destructor")
class Account:
    def __init__(self,num):
        self.account_number=num
        self.obj1=Employee(self)
    def __del__(self):
        print("Account class destructor called")
ac=Account()
del ac
time.sleep()    


