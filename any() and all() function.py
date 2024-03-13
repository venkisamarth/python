print(bool(None))
 
print(bool(1))
print(bool(" "))
# print(bool[1,2,43,4,4])
list1=[0,0,0,0,0,0,1,0,1,0]
print(any(list1))
list1=[0,0,0,None,0]
print(any(list1))
print(all(list1))
list2=[123,'hello']
print(all(list1))


# pytho progam to for sublist present or not  
my_list=eval(input("Enter a list"))
for ele in my_list: 
    print([isinstance(ele,list) for ele in my_list])
else:
    print("sublist not present")
    
