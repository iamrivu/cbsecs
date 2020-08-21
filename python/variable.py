# int
x = 5
# string
y = "John"
print(x)
print(y)

# Assign Value to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# global variable ex1
def myfunc():
  global x
  x = "fantastic from one"
myfunc()
print("Python is " + x) 

# global variable ex2
x = "awesome from two"
def myfuncnew():
  x = "fantastic from two"
  print("Python is " + x)
myfuncnew()
print("Python is " + x)