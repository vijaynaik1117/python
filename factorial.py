'''
num = 7
fact = 1
for i in range(1, num+1):
    fact *= i
print(fact)
'''
def fact(n):
    if n < 2:
        return 1
    else:
        return n * (fact(n-1))
result = int(input("enater a number: "))
print(f"Factorial of {result} is {fact(result)}")
    
 


