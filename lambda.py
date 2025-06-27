'''
def add(a,b):
    return a + b

print(add(2,3))
'''

add = lambda a,b : a + b
print(add(5,4))


### filter

ans = set(filter(lambda a : a%2==0, range(11)))
print(ans)
bns = tuple(filter(lambda a : a%2==0, range(11)))
print(bns)
cns = list(filter(lambda a : a%2==0, range(11)))
print(cns)

