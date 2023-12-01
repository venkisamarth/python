def sum1(*num):
    sum=0 
    for i in num:
        sum=+i
    print(sum)

sum1(10,20)
sum1(10,20,30)
sum1(10, 20,30,40)

#variable lenght keyword argument
def sum1(** num):
    sum=0 
    for key in num:
        sum=sum+num[key]
    print(sum)
sum1(num1=10,num2=20)
sum1(num1=10,num2=30)
sum1(20,30,40)
