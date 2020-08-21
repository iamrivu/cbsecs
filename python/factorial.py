# Using a For Loop
# n = input("Enter a number: ")
n = 5
factorial = 1
if int(n) >= 1:
    for i in range (1,int(n)+1):
        factorial = factorial * i
print("Factorail of ",n , " is : ",factorial)


# Using Recurssion
"""
The process in which a function calls itself directly
or indirectly is called recursion and the corresponding function is called as recursive
"""
num = 5
def recur_factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ("NA")
    else:
        return n*recur_factorial(n-1)
    print (recur_factorial(int(num)))


# Using math.factorial()
import math
num = 5
print("The factorial of ", num, " is : ")
print(math.factorial(int(num)))