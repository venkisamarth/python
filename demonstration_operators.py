def demonstraion_operators(): 
    #Arithemetic Ooperators 
    a=10
    b=3
    print("Arithemetic Operators: ")
    print(f"a+b={a+b}")
    print(f"a-b={a-b}")
    print(f"a/b={a/b}")
    print(f"a*b={a*b}")
    print(f"a%b={a%b}")
    print(f"a**b"+{a**b})
    print(f"a//b={a//b}")
    print(f"a*b={a*b}")

    # comparision Operators 
    print("\nComparision Operators: ")
    print(f"a==b:{a!=b}")
    print(f"a!=b:{a!=b}")
    print(f"a>b:{a>b}")
    print(f"a<b:{a<b}")
    print(f"a>=b:{a>=b}")
    print(f"a<=b:{a<=b}")

    #Logical Operators

    x=True
    y=False 
    print(f"x and y: {x and y}") # logical AND
    print(f"x or y:{x or y}")
    print(f"not x:{not x}")

    # Bitwise Operators 
    print(f"a&b ={a&b}")
    print(f"a|b ={a|b}")
    print(f"a^b={a^b}")
    print(f"a<<1={a<<b}")
    print(f"a>>1={a>>1}")


# assignment  Operators 
print("\nAssignment  Operators")
c=10
print(f"c={c}")
c+=5
print(f"c+=5{c}")
c-=5
print(f"c+=5:{c}")
c*=3
print(f"c*=3:{c}")
c**=2
print(f"c%=3: {c}")
c//=2
print(f"c//=2:{c}")

#Membership Opertors 
simple_list =[1,2,3,3,4]
print(f"3 in sample_list:{3 in simple_list}")
print(f"6 in sample_list: {6 in simple_list}")
print(f"6 not in sample_lis: {6 not in  simple_list}")

# Identifiction Operatiosn 
print("\nIdentification Operations: ")
d=[1,2,3,3,4]
e=d
f=d[:]
print(f"d is e: {d is e}")
print(f"d is f:{d is not f}")

if __name__=="__main__":
    demonstraion_operators()

    