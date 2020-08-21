"""
Python program to count the frequency of 
elements in a list using a dictionary 
"""
# EX 1
def CountFrequency(my_list): 
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
  
    for key, value in freq.items(): 
        print ("% d : % d"%(key, value)) 
  
# Driver function 
if __name__ == "__main__":  
    my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2] 
  
    CountFrequency(my_list)

print("\n")

# EX 2 using count
def CountFrequencyNew(my_list): 
    # Creating an empty dictionary  
    freq = {} 
    for items in my_list: 
        freq[items] = my_list.count(items) 
      
    for key, value in freq.items(): 
        print ("% d : % d"%(key, value)) 
  
# Driver function 
if __name__ == "__main__":  
    my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2] 
    CountFrequencyNew(my_list) 

print("\n")

# EX 3
list = ['a','b','a','c','d','c','c']
frequency = {}
for item in list:
   if (item in frequency):
      frequency[item] += 1
   else:
      frequency[item] = 1
for key, value in frequency.items():
   print("% s -> % d" % (key, value))

print("\n")

# EX 4 using count
list = ['a','b','a','c','d','c','c']
frequency = {}
for item in list:
   frequency[item] = list.count(item)
for key, value in frequency.items():
   print("% s -> % d" % (key, value))