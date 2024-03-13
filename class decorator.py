class Decorator(object): 
    def __init__(self,func): 
        self.function=func
    def  __call__(self,*args): 
        try: 
            if any([isinstance(i,str) for i in args]): 
                raise TypeError("cannot pass string as arguments ")
            else: 
                return self.function(*args)
        except Exception as obj: 
            print(obj)
@Decorator
def add(*args): 
    sum1=0 
    for num in args: 
        sum1=sum1+num
    return sum1 
print(add(10,20,30))        