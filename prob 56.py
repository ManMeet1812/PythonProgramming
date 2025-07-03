tup = (10, 54, 30, 23, 50)
max_tup = max(tup)
print("Maximum Element: ",max_tup)

min_tup = min(tup)
print("Minimum Element: ",min_tup)


tup = (19, 5, 50, 67, 100, 43)
sort_tup = sorted(tup)
print(sort_tup)
print("Maximum Element: ",sort_tup[-1])
print("Minimum Element: ",sort_tup[0])

'''
tup = (19, 15, 50, 60, 100, 40)
sort_tup = sorted(tup)
for i in range(len(tup)):
    while len(tup)!=0:
        if(tup[i]<tup[i+1]):
            print(tup[i])
'''

test_tup = (20, 12, 45, 6, 8, 10)
res=[]
test_tup = list(sorted(test_tup))

k=2

for idx, val in enumerate(test_tup):
    if idx<k or idx >= len(test_tup)-k:
        res.append(val)
res = tuple(res)
print(str(res))
