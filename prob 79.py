def Common(a,b):
    return any(i in b for i in a)

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(Common(a,b))

a1 = [1, 2, 3, 4, 5]
b1 = [6, 7, 8, 9]
print(Common(a1,b1))