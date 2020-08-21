# Compute the greatest common divisor (GCD)
import math 

print ("The GCD of 60 and 48 is : ",end="") 
print (math.gcd(60,48)) 


# Compute the least common multiple (LCM)
# Recursive function to return gcd of a and b 
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a*b) / gcd(a,b) 
  
# Driver program to test above function 
a = 15 
b = 20
print('The LCM of', a, 'and', b, 'is :', lcm(a, b)) 