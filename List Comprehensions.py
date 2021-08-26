num = [1,2,3,4,5]

result = [x*x for x in num]        # map alternative

print(result)

result = [x for x in num if x%2==0]     # filter alternative

print(result)