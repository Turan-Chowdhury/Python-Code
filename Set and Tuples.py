#------------------Tuples-------------------

students = (("Anisul Islam",21,3.56), "turan", "aziz")

print(students)
print(students[1])
print(students[1:])

#---------------Sets---------------------

num1 = {1,2,3,4,5,5}
num2 = set([4,5,6])

print(num1)

num2.add(7)
print(num2)
num2.remove(7)

print(8 in num2)
print(8 not in num2)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)