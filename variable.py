#A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)

x=5
y="john"
print(x)
print(y)

x=2
x="salary"
print(x)

x=str(3)
y=int(3)
z=float(3)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))


x,y,z="pc","laptop","desktop"
print(x)
print(y)
print(z)

x=y=z="orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x="awesome"
print("Python is :" +x)

x="python is "
y="awesome"
z=x+y
print(z)

#Global Variables

x="awesome"
def myfunction():
    print("python is : " +x)
myfunction()

x="awesome"
def function():
    x="fantastic"
    print("Python is " +x)
function()

def function():
    global x
    x="infracture"
function()
print("Our result is :" + x)



