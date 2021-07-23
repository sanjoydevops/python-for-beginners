try:
    print(x) ##The try block will generate an error, because x is not defined:
except:
    print("An exception occured")


try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


try:
    print(x)
except:
    print("Something weent wrong")
finally:
    print("Try and except is finished")


try:
    f=open("s1.txt")
    f.write("sanjoy deb")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()




