student = {
    "101" : "Anisul Islam",
    "102" : "Turan",
    "103" : "Zia",
    104 : "Aziz"
}

print(student["101"])
#print(student["105"])
print(student.get("102"))
print(student.get("105"))
print(student.get("105","Not a valid key"))