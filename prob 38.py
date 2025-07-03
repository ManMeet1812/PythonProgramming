l1 = ["eat", "drink", "sleep", "exercise"]
s1 = "studylstrsc"

obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return Type: ", type(obj1))
print(list(enumerate(l1)))

print (list(s1))
a= len(s1)    
print(list(s1[1]))
print(list(s1[:a]))
print(list(s1[0:(a//2)-1]))
# print(list(s1[a//2:a]))
print(list(s1[a-1 :: -1]))
