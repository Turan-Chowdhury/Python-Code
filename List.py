list = ["C", "C++", "Java", "Python", "Android", "OS"]

print(list)
print(list[0])
print(list[2:])
print(list[2:4])
print(list[:3])
print(list[-1])
print(list[-2])

print("Toc" in list)
print("Toc" not in list)

print(list + ["Toc", 27])
print(list * 3)

print(len(list))

list.append("Toc")
list.insert(2,"BASIC")
list.pop()
list.remove("BASIC")
list.sort()
list.reverse()
list2 = list.copy()
list.clear()


numlist = [20,10,4,555,4,4]

pos = numlist.index(4)
print(pos)
cnt = numlist.count(4)
print(cnt)