#Iterators
list = [1,2,3,4,5,6,7,8,9]
iteration = iter(list)
print(iteration.__next__())
print(iteration.__next__())
print(next(iteration))
# Generator

def fn():
    yield 1
    yield 2
    yield 3

value = fn()
print(value.__next__())
print(value.__next__())
print(value.__next__())