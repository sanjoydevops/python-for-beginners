#Method	Description
#add()	Adds an element to the set
#clear()	Removes all the elements from the set
#copy()	Returns a copy of the set
#difference()	Returns a set containing the difference between two or more sets
#difference_update()	Removes the items in this set that are also included in another, specified set
#discard()	Remove the specified item
#intersection()	Returns a set, that is the intersection of two other sets
#intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	Returns whether two sets have a intersection or not
#issubset()	Returns whether another set contains this set or not
#issuperset()	Returns whether this set contains another set or not
#pop()	Removes an element from the set
#remove()	Removes the specified element
#symmetric_difference()	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	inserts the symmetric differences from this set and another
#union()	Return a set containing the union of sets
#update()	Update the set with the union of this set and others

#Python Sets
myset={"keyboard","mouse","Headphone","VGA","HDMI"}
print(myset)
print(type(myset))

#Duplicates Not Allowed Sets cannot have two items with the same value
myset={"keyboard","mouse","Headphone","VGA","HDMI","Headphone"}
print(myset)
print(len(myset)) #Get the Length of a Set

#Set items can be of any data type
set1={"a","b","c","d"}
set2={1,2,3,4}
set3={True,False,True}
print(set1)
print(set2)
print(set3)

myset={"umbrella",33,True,"Gender",11.44}
print(myset)

#The set() Constructor It is also possible to use the set() constructor to make a set.
myset=set(("Apple","Juce","Orange","Pineapple","Strawbary"))
print(myset)

#Access Items You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword
myset={"Apple","Juce","Orange","Pineapple","Strawbary"}
for x in myset:
    print(x)

#Check if "banana" is present in the set
myset={"Apple","Juce","Orange","Pineapple","Strawbary"}
print("Banana" in myset) 

#Add Items Once a set is created, you cannot change its items, but you can add new items.
myset={"Apple","Juce","Orange","Pineapple","Strawbary"}
myset.add("banana")
print(myset)

#Add Sets To add items from another set into the current set, use the update() method
#Add elements from myset1 into myset
myset={"Apple","Juce","Orange","Pineapple","Strawbary"}
myset1={"Guava","Mango","Papaya"}
myset.update(myset1)
print(myset)

#Add Any Iterable The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
myset={"Apple","Juce","Orange","Pineapple","Strawbary"} #set
myset1=["Guava","Mango","Papaya"] #list

myset.update(myset1)
print(myset)

#Remove Item To remove an item in a set, use the remove(), or the discard() method
myset={"Apple","Juice","Orange","Pineapple","Strawbary"} #set
myset.remove("Juice")
print(myset)

#Loop Items You can loop through the set items by using a for loop

myset={"Apple","Juice","Orange","Pineapple","Strawbary"} 
for x in myset:
    print(x)


#Python - Join Sets

#Join Two Sets You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another

set1={'a','b','c','d'}
set2={1,2,3}
set3=set1.union(set2) #The union() method returns a new set with all items from both sets
print(set3)

set1.update(set2) #The update() method returns a new set with all items from both sets
print(set1)

#Keep ONLY the Duplicates The intersection_update() method will keep only the items that are present in both sets
set1={"Hello","usa","and","washington",1,2,3,False}
set2={"Hello","BD","and","Dhaka",1,3,5,True}
set1.intersection_update(set2)
print(set1)

#The intersection() method will return a new set, that only contains the items that are present in both sets
x={"apple","google","Amazon","Microsoft","Alibaba"}
y={"apple","Azure","GCP","Microsoft","AWS"}
z=x.intersection(y)
print(z)

#Keep All, But NOT the Duplicates
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
x={"apple","google","Amazon","Microsoft","Alibaba"}
y={"apple","Azure","GCP","Microsoft","AWS"}
x.symmetric_difference_update(y)
print(x)

#Return a set that contains all items from both sets, except items that are present in both
x={"apple","google","Amazon","Microsoft","Alibaba"}
y={"apple","Azure","GCP","Microsoft","AWS"}
z=x.symmetric_difference(y)
print(z)




































