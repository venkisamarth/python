class Employee:
    def __init__(self,first,last):
        self.firstname=first
        self.lastname=first
        self.mail=first+last+"@gmail.com"
    @fullname.setter
    def fullname(self):
        return f'{self.firstname}{self.lastname}'
    @fullname.setter
    def fullname(self,name):
        first,last=name.split()
        self.firstname=first
        self.lastname=last
    @fullname.deleter
    def fullname(self):
        self.firstname=None
        self.lastname=None
        e.firstname="jay"
    @property
    def fullname(self):
        return f"{self.firstname}{self.lastname}"
    def mail(self):
        return f"{self.firstname}{self.lastname}@gmail.com"
e=Employee("shantanu","jaiswall")
e1=Employee("venk","samarth")
e3=Employee("raju","naiker")
e.fullname="virat kohli"
print(e1.__dict__)
print(e3.__dict__)
print(e1.firstname)
e.firstname="jay"
print(e.firstname)
print(e.mail)
print(e.fullname)
print("-"*50)
print(e1.mail)
print(e1.firstname)
print(e1.firstname)
print(e1.fullname)
print("__"*50)
#for this we shouldproven the method   for  each method
