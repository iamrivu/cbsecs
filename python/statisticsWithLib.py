"""
Mean - The average value
Median - The mid point value
Mode - The most common value
"""
# Mean
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x) 

# Median
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x) 

# Mode
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x) 