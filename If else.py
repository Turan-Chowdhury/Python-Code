mark = 75

if mark>=80:
    print("A+")
elif mark>=70:
    print("A")
elif mark>=60:
    print("A-")
elif mark>=50:
    print("B")
elif mark>=40:
    print("C")
elif mark>=33:
    print("D")
else:
    print("Fail")

#----------------------------------------------------------------------------------------------------

num1 = 23
num2 = 32

print(num1 if num1>num2 else num2)

max = num1 if num1>num2 else num2
print(max)