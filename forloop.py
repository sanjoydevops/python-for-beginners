
fruits = ["Apple", "Banana", "Cherry"]
for x in fruits:
    print(x)

for x in "Banana":
    print(x)
#for loop using break

hardware=["Monitor", "HDD", "SSD", "RAM", "usb","Pendrive"]
for h in hardware:
    print(h)
    if h=="RAM":
        break
#for loop using continue

food=["Barger", "Fizza", "Rice", "FrideRice", "Chicken"]
for f in food:
    if f=="Rice":
        continue
    print(f)    

#for loop using range

for x in range(6):
    print(x)

for a in range(1,6):
    print(a)

for b in range(2,30,3):
    print(b)

#Else,range using for loop
for c in range(6):
    print(c)
else:
    print("Finished this program")

#if,else,range using for loop
for x in range(6):
    if x==3:
        print(x)
    else:
        print("Successful")

#nested for loop
color=["Red", "Green", "Yellow", "Brown"]
fruit=["Apple", "banana", "Mango", "Fineapple"]
for c in color:
    for f in fruit:
        print(c,f)
#pass
for x in [0,1,2]:
    pass

