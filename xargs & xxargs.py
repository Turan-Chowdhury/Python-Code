#----------------------------------xargs--------------------------------------

def student(*details) :
    print(details)
    print(details[1])

student(101,"turan",3.85)

def add(*numbers) :
    sum = 0
    for num in numbers :
        sum += num
    print(sum)

add(10,20,30)

#---------------------------------xxargs---------------------------------------

def student(**details) :
    print(details)
    print(details["id"])
    print(details["name"])

student(id=101, name="turan")