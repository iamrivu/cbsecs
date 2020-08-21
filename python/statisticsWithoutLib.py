# calculate Mean, Median and Mode with Python without using external libraries.

# Mean : The mean is the average of all numbers and is sometimes called the arithmetic mean. 
# This code calculates Mean or Average of a list containing numbers
n_num = [1, 2, 3, 4, 5] 
n = len(n_num) 
get_sum = sum(n_num) 
mean = get_sum / n 
print("Mean / Average is: " + str(mean)) 

# Median : The median is the middle number in a group of numbers. 
# This code calculates Median of a list containing numbers
n_num = [1, 2, 3, 4, 5] 
n = len(n_num) 
n_num.sort() 
if n % 2 == 0: 
    median1 = n_num[n//2] 
    median2 = n_num[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = n_num[n//2] 
print("Median is: " + str(median)) 

# Mode : The mode is the number that occurs most often within a set of numbers. 
# This code calculates Mode of a list containing numbers
from collections import Counter 
n_num = [1, 2, 3, 4, 5, 5] 
n = len(n_num) 
data = Counter(n_num) 
get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
if len(mode) == n: 
    get_mode = "No mode found"
else: 
    get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
print(get_mode) 