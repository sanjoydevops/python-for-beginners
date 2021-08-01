#Print First 10 natural numbers using while loop

sum=0
while sum<=10:
    print(sum)
    sum=sum+1

#Print the following pattern

lastnumber=6
for row in range(1,lastnumber):
    for column in range(1,row+1):
        print(column,end=' ')
    print(" ")

n=5
k=5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()