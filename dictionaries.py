#Method	Description
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary

#Dictionaries 
mobile = {
    "Brand" : "Nokia",
    "Model" : 1110,
    "Year"  : 2005
}
print(mobile)
#Duplicates not allowed in Dictionaries 
food={
    "vegetable" : "Green chili",
    "Barger" : "Chicken barger",
    "Price" : 150.05,
    "Price" : 10.05
}
#print (food)
print(len(food))
print(type(food))

#Dictionaries Item Data type
accessories = {
    "Brand" : "hp",
    "VGA" : False,
    "HDMI" : True,
    "Year" : 2020,
    "color" : ["Red","Green","Silver"]
}
print(accessories)
print(type(accessories))
#Access Dictionary Items
fruits={
    "Apple" : 220,
    "wait" : "1K",
    "Date" : "19/07/2021"
}
#print(fruits)
#x=fruits["Date"]
#x=fruits.get("Apple")
#x=fruits.keys()
x=fruits.values()
print(x)

#Get Keys The keys() method will return a list of all the keys in the dictionary.
car={
    "Brand" : "Rolseroise",
    "Model" : "v2",
    "Year" : 2019
}
x=car.keys()
print(x)
car["color"] = "Black"
print(x)

#Get Values The values() method will return a list of all the values in the dictionary.

vechils={
    "car" : "ferari",
    "model" : "ferari v2",
    "color" : "silver",
    "year" : 2010
}
print(vechils)
x=vechils.values()
vechils["year"] = 2020
print(x)

#Get Items The items() method will return each item in a dictionary, as tuples in a list.
samsung={
    "Mobile" : "Samsung",
    "Model" : "S3 mini",
    "Color" : "White deep",
    "Year" : 2014
}
s=samsung.items()
print(s)
samsung["color"] = "Deep blue"
print(s)

#Check if Key Exists To determine if a specified key is present in a dictionary use the in keyword:

nokia_pn={
    "Mobile" : "nokia",
    "Model" : "S3 mini",
    "Color" : "White deep",
    "Year" : 2014
}
if "Model" in nokia_pn:
    print("YES Model is one of this dictionary")
#Change ValuesYou can change the value of a specific item by referring to its key name:
computer={
    "Brand" : "HP",
    "Model" : "hp pavilion g6",
    "color" : "silver deep",
    "Year" : 2011
}
computer["Year"] = 2018
print(computer)
computer.update({"Year":2020})  #Update Dictionary The update() method will update the dictionary with the items from the given argument
print(computer)

computer["color"] = "red" #Adding Items
print(computer)

computer.pop("Model") #Removing Items
print(computer)

computer.popitem() #The popitem() method removes the last inserted item 
print(computer)

del computer["Brand"] #The del keyword removes the item with the specified key name
print(computer)

#computer.clear() #The clear() method empties the dictionary
#print(computer)

#Loop Dictionaries
brand = {
    "samsung" : "mobile",
    "HP" : "computer",
    "Nokia" : "mobile",
    "Konka" : "freeze"
}
for x in brand: #Print all key names in the dictionary, one by one
    print(x)
for x in brand: #Print all values in the dictionary, one by one
    print(brand[x])

for a in brand.keys(): #Print all key names in the dictionary, one by one
    print(a)
for b in brand.values(): #Print all values in the dictionary, one by one
    print(b)   

for x,y in brand.items(): #both keys and values, by using the items() method
    print(x,y)

computer={
    "Brand" : "HP",
    "Model" : "hp pavilion g6",
    "color" : "silver deep",
    "Year" : 2011
}
pc=computer.copy()
print(pc)

#Nested Dictionaries
family={
    "children1" : {
        "name" : "Babu",
        "Date of Birth" : "2001 jun 01",
        "Gender" : "male"
    },
    "clildren2" : {
        "name" : "Borsha",
        "Date of Birth" : "2005 july 20",
        "Gender" : "female"
    },
    "clildren3" : {
    "name" : "Borsha",
    "Date of Birth" : "2005 july 20",
    "Gender" : "female"
    }
}
print(family)
for x in family.values():
    print(x)
for y in family.keys():
    print(y)
for x,y in family.items():
    print(x,"=",y)









