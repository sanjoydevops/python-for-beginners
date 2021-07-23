def my_function():
    print("Hello world")
my_function()

def my_function(fname):
    print(fname + " Hello ")
my_function("email")
my_function("Name")
my_function("age")

def sum():
    a=10
    b=20
    c=30
    d=a+b+c
    return d
print("Total summation",sum())

#Arguments in function
def myfun(name):
    print("HI",name)
myfun("sanju")

# def MyFunction(a,b):
#     return a+b
# a=int(input("Enter a :"))
# b=int(input("Enter b :"))
# print("sum =",MyFunction(a,b))


#Passing Immutable Object (List)
def chnage_list(list1):
    list1.append(200)
    list1.append(300)
    print("List inside function =",list1)

list1=[10,20,30,40]
chnage_list(list1)
print("list outside function =",list1)

def printme(*names):
    print("types of passed arguments is",type(names))
    print("printing the passed arguments.....")
    for name in names:
        print(name)
printme("john","David","smith","nick")


def add(num1,num2):
    return num1+num2

sum=add(100,200)
print(sum)



