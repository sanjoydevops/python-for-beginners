x=lambda a : a+10
print(x(5))

x=lambda a,b,c : a+b+c
print(x(2,6,2))

def myfunction(n):
    return lambda a: a*n
mydoubler=myfunction(2)
print(mydoubler(11))


def myfun(n):
    return lambda a:a*n
mydoubler=myfunction(2)
mytripler=myfunction(3)
print(mydoubler(11))
print(mytripler(11))

