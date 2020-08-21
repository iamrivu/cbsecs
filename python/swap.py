# simple swap
a = 5
b = 6

temp = a
a = b
b = temp

print(a)
print(b)

# using xor it will not use extra bit like temp
a = 10
b = 11

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)

# only in python
a = 15
b = 16

# works only in same line (it's goes into stack and reverse)
a,b = b,a

print(a)
print(b)