try :
    list = [20,0,30]
    result = list[0] / list[3]
    print("Done")
except ZeroDivisionError :
    print("Dividing by zero is not possible")
except IndexError :
    print("Index error")
except TypeError :
    print("Type error")
finally :
    print("Successful")


