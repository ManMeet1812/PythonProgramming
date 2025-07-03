strng = "This is a python Language"
strn = strng.split(' ')
print(strn)

for i in strn:
    if (len(i) % 2 == 0):
        print(i)