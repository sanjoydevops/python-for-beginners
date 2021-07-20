#new_list = [expression for member in iterable]
#new_list = [expression for member in iterable (if conditional)]
#new_list = [expression (if conditional) for member in iterable]

fruit=["apple","banana",'cherry','kiwi','mango']
b= [x for x in fruit]
print(b)

fruit=["apple","banana",'cherry','kiwi','mango']
newlist=[x for x in fruit if "a" in  x]
print(newlist)

val= [x for x in range(10) if x<5]
print(val)

fruit=["apple","banana",'cherry','kiwi','mango']
newlist=[x for x in fruit if x!="apple"]
print(newlist)

fruit=["apple","banana",'cherry','kiwi','mango']
newlist=[x.upper() for x in fruit] #Set the values in the new list to upper case
newlist1=[x.lower() for x in fruit] #Set the values in the new list to lower case
print(newlist)
print(newlist1)

fruit=["apple","orange","banana",'cherry','kiwi','mango']
newlist1=["Hello" for x in fruit] #Set all values in the new list to 'hello'
print(newlist1)

fruit=["apple","orange","banana",'cherry','kiwi','mango']
newlist=[x if x != "banana" else "orange" for x in fruit]
print(newlist)

#Sort List Alphanumerically List objects have a sort() method that will sort the list alphanumerically, ascending, by default
fruit=["apple","orange","banana",'cherry','kiwi','mango']
fruit.sort()
print(fruit)

num=[100,90,85,20,50,30,70,80]
num.sort()
print(num)

#Sort Descending
fruit=["apple","orange","banana",'cherry','kiwi','mango']
fruit.sort(reverse=True)
print(fruit)

num1=[10,20,30,40,50,60,70,100]
num1.sort(reverse=True)
print(num1)

#Copy a List
fruit=["apple","orange","banana",'cherry','kiwi','mango']
fruit_list=fruit.copy()
print(fruit_list)

#Join Two Lists
list1=['a','b','c','d']
list2=[1,2,3,4]
list3=list1+list2
print(list3)

#Join Two Lists using for loop
list1=['a','b','c','d']
list2=[1,2,3,4]
for x in list2:
    list1.append(x)
print(list1)

#Join Two Lists using extend
list1=['a','b','c','d']
list2=[1,2,3,4]
list1.extend(list2)
print(list1)





