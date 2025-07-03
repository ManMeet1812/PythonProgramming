import sys

list = [10, 34, 54, 60]

st = {10, "Harsh", 30, "Manmeet"}
set_lst = set(list)
print(set_lst)
print(sys.getsizeof(set_lst), "bytes")
print(st.__sizeof__())

