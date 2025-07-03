def cube(x):
    return x*x*x

print(cube(5))

cube1 = lambda x: x*x*x
print(cube1(6))

lst = [12, 32, 20, 5, 10]
res = []
for i in lst:
    res.append(cube1(i))
    
print(res)

lst = [12, 2, 10, 5, 11]
newl = map(cube, lst)
new_l = list(map(cube, lst))
print(newl)
print(new_l)


def filter_func(a):
    return a>8
newl = list(filter(filter_func, lst))
print(newl)

lst = [12, 20, 10, 15, 11]

new_l = list(map(lambda x: x*x*x, lst))
#print(newl)
print(new_l)
