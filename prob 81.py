lst = [20, 30, 16, 70]
lst2 = lst[0]
for i in lst:
   if (lst2>i):
       lst2 = i
       
print(lst2)

########################################################
lst = [1, 5, 8, 9, 6]
for i in lst:
    res = []
    idx = lst.index(i)
    for j in range(len(lst)):
        if (idx == j):
            continue
        res.append(i<lst[j])
    print(res)
    
############################################################
    
lst = [20, 15, 16, 5]
lst2 = lst[0]
for i in lst:
   if (lst2>i):
       lst2 = i
       
print(lst2)
