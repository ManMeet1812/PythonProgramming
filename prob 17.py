test_list = ['gfg', 'is', 'best', 'for','geeks']
print("The original list is : ", test_list)

res = [sub.replace('g','-').replace('e','g').replace('-','e') for sub in test_list]
print("The replaced list is : ", res)



lst = ['gfg', 'is', 'best', 'for','geeks']
print("The original list is : ", test_list)
res = ",".join(lst)
res = res.replace('g','-').replace('e','g').replace('-','e').split(',')
print("The replaced list is : ", res)

