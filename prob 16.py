test_list = [1, 4, 5, 7, 8]
print("The list is:",test_list)

list_len = sum(1 for i in test_list)
print("The length of list is:",list_len)


# Another method
from collections import Counter

second_lst = [12, 45, 65, 8, 10, 15, 50]
print("The list is:",second_lst)

lst_len = sum(Counter(second_lst).values())
print("The length of list is:",lst_len)

# One more method

third_lst = [12,13,15,16,17,18,19,20,21,22,23,24,25]
print("The list is:",third_lst)
lis_len1 = sum(1 for _ in third_lst)
print("The length of list is:",lis_len1)

# last method recursion
def rec_len(lst):
    if not lst:
        return 0
    else:
        return 1+rec_len(lst[1:])
    
lst= [1, 2, 3, 4]
print("The list is:",lst)
print("The length of list is:",rec_len(lst))

