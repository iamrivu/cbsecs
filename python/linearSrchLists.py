"""
A simple approach is to do linear search, i.e
1) Start from the leftmost element of list and one by one compare x with each element of the list.
2) If x matches with an element, return True.
3) If x doesn’t match with any of elements, return False.
"""
# Search function with parameter list name 
# and the value to be searched 
def search(list,n): 
  
    for i in range(len(list)): 
        if list[i] == n: 
            return True
    return False
  
# list which contains both string and numbers. 
list = [1, 2, 'sachin', 4,'Geeks', 6] 
  
# Driver Code 
n = 'Geeks'
  
if search(list, n): 
    print("Found") 
else: 
    print("Not Found") 