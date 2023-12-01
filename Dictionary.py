#Unordered key-value pairs.
#Keys are immutables (numbers, strings,tupls). tuples).
#Values can be any object.
user={}
user["name"]="Footbar"
print(user)
user["email"]='footbar.com'
print(user)
the_name=user['name']
print(the_name)
field="name"
the_velue=user[field]
print(the_velue)

user['name']="Eidth piaf"
print(user)
#keys
user={
    "fname":"foo",
    "lname":"bar",

}
print(user)
print(user.keys())
#Loops over the keys
user={
    "fname":"venki",
    "lname":"Bar",
}
for k in user.keys():
    print(k)
for k in user.keys():
    print(k)  
#loops using items 
people={
    "foo":"123",
    "bar":"456",
    "qux":"789",
}
for name,uid in people.items():
    print("{}=>{}".format(name,uid)) 
user={
    "fname":"foo",
    "lname":"bar",
    }       
for t in user.items():
    print("{}->{}".format(t[0],t[1]))
    print(("{}->{}".format(*t)))