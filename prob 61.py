my_Dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
myKeys = list(my_Dict.keys())
myKeys.sort()
sorted_dict = {i: my_Dict[i] for i in myKeys}
print(sorted_dict)
    
    
#############################################################
from collections import OrderedDict

dict = {'ravi': '10', 'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)