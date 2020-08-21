"""
Python offers to compute the power of a number and hence can make 
task of calculating power of a number easier
"""
# EX 1 without pow()/native method to compute power
n = 1
for i in range(1,5): 
    n=3*n 
  
print ("The value of 3**4 is : ",end="") 
print (n) 

print("\n")

# EX 2 with Pow() to compute power

# 1. float pow(x,y) : This function computes x**y. 
# This function first converts its arguments into float and then computes the power
print ("The value of 3**4 is : ",end="")
print (pow(3,4)) 

# 2. float pow(x,y,mod) : This function computes (x**y) % mod. 
# This function first converts its arguments into float and then computes the power.
print ("The value of (3**4) % 10 is : ",end="")
print (pow(3,4,10))

# 3. Implementation Cases in pow().

# Python code to discuss negative 
# and non-negative cases 
# positive x, positive y (x**y) 
print("Positive x and positive y : ",end="") 
print(pow(4, 3)) 
print("Negative x and positive y : ",end="") 
# negative x, positive y (-x**y) 
print(pow(-4, 3)) 
print("Positive x and negative y : ",end="") 
# positive x, negative y (x**-y) 
print(pow(4, -3)) 
print("Negative x and negative y : ",end="") 
# negative x, negative y (-x**-y) 
print(pow(-4, -3))