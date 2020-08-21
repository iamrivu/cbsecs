"""
 In math, divisibility refers to a number's quality of being evenly divided by another number, 
 without a remainder left over
"""
# EX 1
# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]
# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))
# display the result
print("Numbers divisible by 13 are",result)

# EX 2
# Function to check whether a number is divisible by 7 
def isDivisibleBy7(num) : 
    # If number is negative, make it positive 
    if num < 0 : 
        return isDivisibleBy7( -num ) 
  
    # Base cases 
    if( num == 0 or num == 7 ) : 
        return True
      
    if( num < 10 ) : 
        return False
          
    # Recur for ( num / 10 - 2 * num % 10 )  
    return isDivisibleBy7( num / 10 - 2 * ( num - num / 10 * 10 ) ) 
      
# Driver program 
num = 616
if(isDivisibleBy7(num)) : 
    print ("Divisible")
else : 
    print ("Not Divisible")