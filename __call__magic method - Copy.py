#callable():
#True: if the object is callable
#False:  if tha object is not callable
#what are callable object?
#object which can be called  whenver we required is called as the callable object
#objects having __call__methid in there 
x=100
def add(a,b):
    return a+b
print(type(add))
print(callable(x))
print(callable(add))
print(add(20,30))
print(add(29,39))
print(add.__call__(10,20))
print(callable(x))
print(callable(add))
########################
class Add(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b 
#a1=Add(10,20)
#print(callable(Add))
#print(callable(a1))

###########################
class Add(object):
    def __init__(self,a,b):
        self.a=a 
        self.b=b 
    def __call__(self):
        print("hello")
a1=Add(10,20)
a1()
print(callable(a1))



