for i in range(1,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print()

first=[1,2,3,4,5]
second=[20,30,40]
final=[]
for i in first:
    for j in second:
        final.append(i+j)
print(final)