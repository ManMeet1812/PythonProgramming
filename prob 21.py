lst= [100, 55, 60, 12, 45]
b= 55
for i, x in enumerate(lst):
    lst[i]=x
    print(lst[i])
    if x==b:
        print(b, "is in list.")
    else:
        print(b, "is not in list.")

# 2nd method
lst= [100, 45, 65, 12, 30]
b=12
if b in lst:
    print(b, "is in list.")
    
else:
    print(b, "is not in list.")
    
#3rd method
test_list = [1, 6, 3, 5, 3, 4]
 
# Checking if 4 exists in list
for i in test_list:
    if(i == 4):
        print("Element Exists")
        
# 4th method
list1 = [10, 15, 18, 46, 50, 5]
cnt=list1.count(11)
if cnt>=1:
    print("Element Exists")
else:
    print("Element  does not Exist")
    
#5th method
from collections import Counter
lst = [15, 16, 17, 18]
freq=Counter(lst)
print(freq)
if freq[20]>0:
    print("Element Exists")
else:
    print("Element  does not Exist")
    
def eleinlst(lst, element):
    try:
        lst.index(element)
        return True
    except ValueError:
        return False

t_lst = [1,2,4,7,10,5]
print(eleinlst(t_lst, 5))
print(eleinlst(t_lst, 8))

# 6th method
def chk_ele(lst, target):
    return target in set(lst)

lst = [23, 45, 54, 12, 10]
tar = 3
print("Exists using set: ", chk_ele(lst, tar))
    
