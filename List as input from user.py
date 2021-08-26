n = input("Enter a text of numbers : ")

list = n.split()
sum = 0

for x in list:
    sum = sum + int(x)

print(sum)

#--------------------------------------------

numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a text : ")

for x in text:
    x = x.lower()
    if x>='a' and x<='z':
        numOfLetters+=1
    elif x>='0' and x<='9':
        numOfDigits+=1
    elif x==' ':
        numOfWords+=1

print(numOfLetters)
print(numOfDigits)
print(numOfWords+1)