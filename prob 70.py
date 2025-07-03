def Merge(dic1, dic2):
    for i in dic2.keys():
        dic1[i]=dic2[i]
        return dic1


dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"G": 5, "K": 9, "E": 10}
print(Merge(dic1, dic2))

#################################################
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = ChainMap(dict1, dict2)
print(merged_dict)