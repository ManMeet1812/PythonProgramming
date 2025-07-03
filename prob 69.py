def Merge(dic1, dic2):
    return(dic2.update(dic1))


dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"G": 5, "K": 9, "E": 10}



print(Merge(dic1, dic2))
print(dic2)

#######################################################
def Merge(dic1, dic2):
    res = {**dic1, **dic2}
    return res
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

#########################################################
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = dict1 | dict2
print(dict3)

