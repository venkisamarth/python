# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "occupation": "Engineer"
}

# Accessing values using keys
print(person["name"])  # Output: "John"

# Modifying values
person["age"] = 31
print(person["age"])   # Output: 31

# Adding new key-value pairs
person["location"] = "New York"

# Deleting a key-value pair
del person["occupation"]

#Storing person inforamation
person1 ={"name":"John","age":30,"Occupaton":"Engineer"}
person2={"name":"Alice","age":25,"occupation":"Teacher"}
people=(person1,person2)
print(people)

#Represeting point as dictionaries in a tuple:
point1={"x":10,"y":20}
point2={"x":-5,"y":15}
point=(point1,point2)

#Storing configuration setting as dictinaries in tuple:
config1={"max_iter":100,"tolerence":1e-6}
config2={"max_iter":200,"tolerence":1e-8}
configuration=(config1,config2)

#using dictionaries to report book information in tuple
book1={'title':"Python crash course","authore":"Eric Matthes","pages":560}
book2={'title':'clean code',"author":"Robert c","pages":465}
books=(book1,book2)
print(books)

#group information about countries in tuple using dictionaries
country1={"name":"USA","Population":3310026,"capital":"washington,D.c"}
country2={"name":"china","population":1444214,"capital":"Beijing"}
countries=(country1,country2)
print(countries)











