def decor(func):
    def inner():
        func()
        print("welcome")
        print("Welcome")
    return inner
@decor
def printer():
    print("welcome")
    print("welcome")
printer()
#example2




def decor(addition):
    def inner():
        result=addition()
        num3=float(input("Enter  the third number:"))
        result=result+num3
        return result
    return inner
@decor
def addition():
    num1=float(input("enter the  first number:"))
    num2=float(input("enter teh second number:"))
    result=num1+num2
    return result
result_function=addition
print(result_function)









