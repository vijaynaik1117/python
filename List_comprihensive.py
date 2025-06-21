'''
in order to make simpler code

x = []
for i in range(11):
    z = i ** 2
    x.append(z)

print(x)

'''
'''
x =[i ** 2 for i in range(11)]
print(x)
'''

# or
'''
x = []
for i in range(11):
    if i%2 == 0:
        z = i ** 2
        x.append(z)

print(x)
'''

x = [i ** 2 for i in range(11) if i % 2 == 0]

print(x)
