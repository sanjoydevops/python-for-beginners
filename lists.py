#Method	Description
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

#python list
fruits=['apple','mango','verry','graps']
print(fruits)

#Allow Duplicates Since lists are indexed, lists can have items with the same value:

fruits=['apple','mango','verry','graps','apple','pine-apple']
print(fruits)
print(fruits[1]) #Access Items
print(fruits[-1]) #Negative Indexing
print(fruits[2:5]) #Range of Indexes
print(fruits[:4])
print(fruits[2:])
if 'apple' in fruits:   #Check if Item Exists
    print("Yes, apple is in the list!!!")

computer=['hp','dell','HDD','ssd','ram','processor','motherboard']
print(computer[-4:-1]) #Range of Negative Indexes

#Change a Range of Item Values
vegetable=['Broccoli','Lettuce','Bitter gourd','Ridge gourd','Cucumber']
print(vegetable)
vegetable[1:3]=['Black current','Watermelon']
print(vegetable)


fruit=['apple','orange','pineapple']
fruit[1:3]=['watermelon'] #Change a Range of Item Values
print(fruit)
fruit.insert(2,'Banana') #The insert() method inserts an item at the specified index
fruit.insert(1,'Guava')
print(fruit)

#Append Items To add an item to the end of the list, use the append() method
electronics=['light','fan','switch','tv','wire']
electronics.append("genarator")
print(electronics)

#Extend List To append elements from another list to the current list, use the extend() method
vegetable=['Broccoli','Lettuce','Bitter gourd','Ridge gourd','Cucumber']
fruit=['apple','orange','pineapple']
vegetable.extend(fruit)
print(vegetable)
#Add Any Iterable The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
computer=("pc","laptop","hp","dell","asus") #tuple
elec=["light","fan","wire"] #list
elec.extend(computer) #print will be the output list
print(elec)

fruit=['apple','orange','pineapple','Guava','Banana','multa','Grups']
fruit.remove("orange") ##The remove() method removes the specified item
print(fruit)
fruit.pop(1) # The pop() method removes the specified index
print(fruit)
fruit.pop() # If you do not specify the index, the pop() method removes the last ite
print(fruit)

#Python - Loop Lists You can loop through the list items by using a for loop
water=["mum","kinla","fresh","starlin","jibon"]
for x in water:
    print("Water company",x)

water=["mum","kinla","fresh","starlin","jibon"]
for x in range(len(water)):
    print(water[x])



























































