x=5
print(type(x))
x="hello world"
print(type(x))

x=20.5
print(type(x))

x=1j
print(type(x))


x=frozenset({"Apple","Mango"})
print(x)
print(type(x))

x=b"Hello"
print(x)

x=bytearray(5)
print(x)

x=memoryview(bytes(5))
print(x)

#Type Conversion
x=1
y=2.4
z=1j

a=float(x)
print(a)
b=int(y)
print(b)
c=complex(x)
print(c)

#Random number
import random
print(random.randrange(1,10))




