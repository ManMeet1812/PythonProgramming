##################################################
test_str = 'geeksforgeeks   33   best'
str1 = test_str.split(' ')
str2 =''.join(str1)
print(len(str2))

#################################################
test_str = 'geeksforgeeks 33    best'

res = sum(not chr.isspace() for chr in test_str)
print(res)
print(str(res))

################################################
test_str = 'geeksforgeeks 33  is best'

new_str = test_str.replace(' ','')
print(new_str)
print(len(new_str))

###################################################
test_str = 'Manmeet Loves Harshdeep'
count=0
for i in test_str:
    if i == ' ':
        continue
    count +=1
    
print(count)

######################################################
test_str1 = 'Manmeet weds Harshdeep'
res = len(''.join([char for char in test_str1 if char != ' ']))
print(res)

######################################################



 
