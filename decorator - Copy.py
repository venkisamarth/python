def decor(addition_func):
    def inner():
        result = addition_func()
        num3 = float(input("Enter the third number: "))
        result += num3
        return result
    return inner

@decor
def addition():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    return result

result_function = addition
print(result_function())


#DEcorator in multiple Decorator
#how to apply multiple decorator for a  function
def decor1(func):
    def inner():
        return func().upper()
    return inner
def decor2(func):
    def inner():
        return func().split()
    return
@decor2
@decor1
def get_name():
    name=input("Enter the first name")
    sirname=input("Enter the sirname")
    full_name=name+" "+sirname 
    return full_name
print(get_name)
