def even(a):
    return a%2==0
number = [1,2,3,4,5,6,7,8,9]
ans = list(filter(even,number))
print(ans) 
ans = set(filter(even,number))
print(ans)  
ans = list(map(even,number))
print(ans) 
ans = set(map(even,number))
print(ans)    