num= int(input("Enter number of elements you want in a tuple: "))
tup = ()
for i in range(0,num):
    a=int(input("Element"+str(i) + ": "))
    tup.append(a[i])
    
print(tup)
    