num1=10
num2=20
print(num1)
print(num2)
print(num1.__add__(num2))
#print(int.__add__(num1,num2))
print(num1.__add__(num2))

#######################
num1="hello"
num2="world"
print(num1+num2)
print(num1.__add__(num2))
print(str.__add__(num1,num2))
print(dir(str))
print(dir(int))
print(dir(str))
print(dir(float))

###################
#operator overloading
class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
b1=Book("one indian girl,",300)
b2=Book("Making indian awsome",200)
#print("total number of pages:", b1+b2)

class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def __add__(self,other):
        total=self.pages+other.pages
        return total
b1=Book("one indain girl",300)
b2=Book("making indain awsome",400)
b3=Book("half girlfriend,",400)
#print("total number of pages:",b1+b2+b3)

#overloding comparision
class total:
    def __init__(self,name,fare):
        self.name=name
        self.fare=fare
    def _get__(self,other):
       return self.fare>other.far
h1=total("Taj hotel",20000)
h2=total("pancahtantra",10000)
print(h1>h2)
print(h1>h2)


    

