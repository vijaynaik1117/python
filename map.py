numbers = [1,2,3,4,5,6,7,8,9]
def square(a):
    return a **2
ans = list(map(square,numbers))
print(ans)

numbers = [1,2,3,4,5,6,7,8,9]
def square(a):
    return a **2
ans = list(filter(square,numbers))
print(ans)


# filter only retun the value paramaeter
# Map pro=vides the funtion output and result