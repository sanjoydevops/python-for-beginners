#Method	Description
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found

#Access Tuple Items
mytuple=("Apple","Banana","Orange","cherry","Apple","Orange")
print(mytuple)
print(mytuple[3])
print(mytuple[-1]) #Negative Indexing
print(mytuple[-4:-1]) #Range of Negative Indexes
print(mytuple[3:]) #Range of Indexes
print(mytuple[2:5]) #Range of Indexes
print(mytuple[:4]) #Range of Indexes

#Check if Item Exists
mytuple=("Apple","Banana","Orange","cherry","Apple","Orange")
if  "Apple" in mytuple:
    print("Yes apple is in there")

#Change Tuple Values Once a tuple is created, you cannot change its values. Tuples are unchangeable
#Convert the tuple into a list to be able to change it

mytuple=("Apple","Banana","Orange","cherry","Apple","Orange")
y=list(mytuple)
y[1]="wiki"
mytuple=tuple(y)
print(mytuple)

#Remove Items
mytuple=("Apple","Banana","Orange","cherry","Apple","Orange")
y=list(mytuple)
y.remove("Apple")
mytuple=tuple(y)
print(mytuple)

""" mytuple=("Apple","Banana","Orange","cherry","Apple","Orange")
del mytuple
print(mytuple) """

#Loop Through a Tuple You can loop through the tuple items by using a for loop
mytuple=("Apple","Banana","Orange","cherry","Apple","Orange")
for x in mytuple:
    print(x)

#Loop Through the Index Numbers
#You can also loop through the tuple items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.

mytuple=("Apple","Banana","Orange","cherry","Apple","Orange")
for x in range(len(mytuple)):
    print(mytuple[x])

#Using a While Loop
mytuple=("Apple","Banana","Orange","cherry","Apple","Orange")
i=0
while i < len(mytuple):
    print(mytuple[i])
    i=i+1

#Join Two Tuples

mytuple1=('a','b','c','d')
mytuple2=(0,1,2,3)
mytuple3=mytuple1+mytuple2
print(mytuple3)

mytuple1=('a','b','c','d')
mytuple=mytuple1*2
print(mytuple)



























