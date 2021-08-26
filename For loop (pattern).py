n = 4

for i in range(1,n+1):
    print("*" * i)

print("---------")

for i in range(1,n+1):
    print("*" * (2*i-1))

print("---------")

space = n-1
star = 1

for i in range(1,n+1):
    for j in range(1,space+1):
        print(" ",end="")
    space-=1
    for j in range(1,star+1):
        if(j==i):
            print("*")
        else:
            print("*",end="")
    star+=1



