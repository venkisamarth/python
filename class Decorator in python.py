
from typing import Any


class Decorator(object):
    def __init__(self,func):
        self.function=func
    def __call__(self,a,b):
        result=self.function(a,b)
        return result**2
@Decorator
def add(a,b):
    return a+b
print(add(2,3))
#####################
#Decorator in python Example
def add(*args):
    sum1=0
    for num in args:
        sum1=sum1+sum1
    return sum1
print(add(10,20,30))
print(add(10,20,30))
class Decorater(object):
    def __init__(self,func):
        self.function=func
    def __call__(self,*args):
        try:
            if any([isinstance(i,str) for i in args]):
                raise TypeError(" cannot pass string arguments")
            else:
                return self.function(*args)
        except Exception as obj:
            print(obj)
@Decorater
def add(*args):
    sum1=0
    for num in args:
        sum1 = sum1+num
        return sum1
print(add(10,20,30))
print(add(20,30,40))


        