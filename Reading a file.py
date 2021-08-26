file = open("student.txt","r+")
print(file.readable())
print(file.writable())
text = file.read()
print(text)
size = len(text)
print(size)
file.close()

file = open("student.txt","r")
text = file.readlines()
print(text)
file.close()

file = open("student.txt","r")
text = file.readlines() [1]
print(text)
file.close()

file = open("student.txt","r")
for line in file :
    print(line)
file.close()