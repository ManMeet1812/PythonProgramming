def Common(a, b):
    set_a = set(a)
    set_b = set(b)
    if len(set_a.intersection(set_b))>0:
        return True
    return False



a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(Common(a,b))

a1 = [1, 2, 3, 4, 5]
b1 = [6, 7, 8, 9]
print(Common(a1,b1))