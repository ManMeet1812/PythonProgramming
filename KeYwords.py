import keyword

print("List of all the Keywords:")
print(keyword.kwlist)


print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)
print(True * True * True)
print(True * False * False)

print(None == 0)
print(None == [])

print(True or False)
print(True and False)

print(not True)

if 's' in 'geeksforgeeks':
    print("s is a part of Geeks For Geeks")
else:
    print("s is not a part of Geeks For Geeks")
    
for i in 'geeksforgeeks':
    print(i)
    
for i in 'geeksforgeeks':
    print(i, end= ' ')
    
print("\r")

#is: This keyword is used to test object identity,
#i.e to check if both the objects take the same memory location or not. 
 
# using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' ' is ' ')
 
# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})

print([] is [])

print(() is ())
    
    