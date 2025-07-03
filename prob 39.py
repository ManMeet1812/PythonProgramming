l1 = ["eat", "drink", "sleep", "exercise"]
s1 = "studylstrsc"

obj1 = enumerate(l1)
obj2 = enumerate(s1)
print(obj1)
print(obj2)

print(type(obj1))
print(enumerate(l1))
print(list(enumerate(l1)))
print(list(enumerate(s1, 0)))

print(list(enumerate(s1)))

print(list(enumerate(s1, 5)))

#############################################################
l1 = ["eat","sleep", "repeat"]
s1 = "studysst"
for ele in enumerate(l1):
    print(ele)
    
for ele1 in enumerate(s1):
    print(ele1)

for i,x in enumerate(l1):
    print(i)
    print(x)
    
for i,x in enumerate(s1):
    print(i, end= '')
    #print('\n')
    print('\n', x, end= '')