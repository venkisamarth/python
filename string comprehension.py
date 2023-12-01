

my_string='Hello World'
print(my_string)

text = "Hello, World!"
result = ''.join(text[i] for i in range(len(text)-1, -1, -1))
print(result)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#creatin the list of squared numbers:
numbers=[1,2,3,4,5,6]
squared_numbers=[num**2 for num in numbers]
print(result)


word = "hello"
uppercase_letters = [char.upper() for char in word]
print(uppercase_letters)  # Output: ['H', 'E', 'L', 'L', 'O']

#Filtering a list to contain only even numbers
numbers=[1,2,3,4,5,6,7,8,8,9,10]

even_numbers=[num for num in numbers if num %2==0 ]
print(even_numbers)


#creating a linght of word in sentence:
senetence="I love coding in python"
word_lengths=[len(word) for word in senetence.split()]
print(word_lengths)

#reversing a string
word="python"
reversed_word=''.join([char for char in reversed(word)])
print(reversed_word)

#creting a list of first characters of word in sentence:
senetence='Python is a powerfull language'
first_chars=[word[0] for word in senetence.split()]
print(first_chars)

#converting the list numbers to sting
numbers=[1,2,3,4,5]
numbers_string=[str(num) for num in numbers]
print(numbers_string)



#creating a list even or odd labels based on numbers
numbers=[1,2,3,4,5,6]
labels=['even' if num % 2 ==0 else  'odd' for num in numbers]
print(labels)

string1 = "Hello"
string2 = "World"
combined = [s1 + s2 for s1 in string1 for s2 in string2]

print(combined) 


numbers = [1, 2, 3, 4, 5]
labels = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(labels)  # Output: ['odd', 'even', 'odd', 'even', 'odd']


numbers=[1,2,3,4,4,5,6,67,7,54]
labels=['even'if num %2==0 else 'odd' for num in numbers]
print(labels)

#combaing letters  from two string
string1="Hello"
string2="World"
combained=[s1 + s2 for s1 in string1 for s2 in string2 ]
print(combained)

word="Python"
reversed_word=''.join([char for char in reversed(word)])
print(reversed_word)

#genrating the string with the first charecter of each word in a sentence
senetence="Pyhton is a powerfull language"
first_chars=''.join(word[0] for word in senetence.split())
print(first_chars)

#concatenationg letter from two string
string1="Hello"
string2="World"
combained=''.join([s1+s2 for s1 in string1 for s2 in string2])
print(combained)



#Comparing string 

#Using the "==" operators:

string1="Hello"
string2="Hello" 
if string1== string2:
    print('String are equal')
else:
    print(":String are not Equal")
#Using the != operator        
string1="Hello"
string2="World"
if string1 != string2:
    print("string are not equal")
else:
    print("sting are equal")   
#Using is operator to check if two  string object refer to the  same memorey locaton
string1="veni"     
string2="venki"

if string1 is string2:
    print("string are the same object")
else:
    print("String are different objects")    
#using 'is not ' operator
string1="hello"    
string2="world"
if string1 is not string2:
    print("string are diffrent  objects")
else:
    print("String are the same object ")
import sys
if sys.version_info.major ==2:
    string1="Hello"    
    string2="Hello"
    if cmp(string1,string2)==0:
        print("string are equal")
    else:
        print("string are not equal")
else:
    print("cmp() function not available in python 3") 
#Using the 'startwith()' method to cherck if a string statrs with a specifix
# prifix
string1="Hello,World"              
prefix="Hello"
if string1.startswith(prefix):
    print("string starts with the prefix")
else:
    print("string does not start with teh prefix")

#Using the endwith() method to check if a string ends with a specifc  suffix:
string1='Hello'
suffix="World"
if string1.endswith(suffix):
    print("String ends with the suffix")
else:
    print("String does not end with the suffix") 
#assigning multiple values from a list to veriable using tuple
#assigning

my_list=[1,2,3,4,5]
a,b, *rest, last= my_list
print(a)
print(b)
print(rest)
print(last)

#assigning default values to veriable suring tuple assignment 
a,b,c=10,20,30
x,y,z=None,None,None
a,b,c = x or a,  y or b,z or c
print(a,b,c)

# tuple assignment with list list comprehesion
nested_list=[[1,2],[3,4],[5,6]]
tuple_list=[(a,b)for [a,b] in nested_list]
print(tuple_list)

#similarity assigning values to multilple variable
a=b=c =10
print(a,b,c)

