test_list = [5, 6, 7]
test_tup = (8, 9)
res =  tuple(list(test_tup) + test_list)
print(res)

########################################################################

test_list = [4, 5, 6, 7, 8]
test_tup = (1, 2, 3)
#test_tup += test_list
test_list += test_tup
print(test_list)

########################################################################

my_list = [45, 67, 15, 80]
my_tuple = (9, 10)
 
index = 3
my_list.insert(index, my_tuple)
print(my_list)