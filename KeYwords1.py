for i in range(10):
    print(i, end=' ')
    if i== 6:
        break
    
print("\r")
    
for i in range(10):
    if i== 6:
        i=+1
        continue
    print(i, end=' ')
    
print("\r")  #newline

k=0
while k<= 10:
    if k==6:
        k+=1
        continue
        print(k, end=' ')
    else:
        print(k, end=' ')
    k+=1
    
print("\r")
    
i = 0
while i < 10:
 
    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        i += 1
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")
 
    i += 1
    
print("\r")

n = 10
for i in range(n):
 
    # pass can be used as placeholder
    # when code is to added later
    pass

print("\r")

i = 20
if i==20:
    print ("i is Twenty")
elif i==10:
    print ("i is not Twenty")
else:
    print ("i is not Present")
    