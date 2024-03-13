#there are two types of decorater 
# function decorator 
# class decorater 

class decorater(object):
    def __init__(self,func): 
        self.function=func
    def __call__(self,a,b): 
        result=self.function(a,b)
        return result**2 
@decorater 
def add(a,b): 
    return a+b
print(add(1,2))

