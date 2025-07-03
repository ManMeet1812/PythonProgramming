dic =  {'a': 100, 'b':200, 'c':300}

dic_items = dic.values()
print(dic_items)
print(sum(dic_items))

#####################################################3
dic1 =  {'a':400, 'b':200, 'c':600}

dic1_items = dic1.values()
count = 0
for i in dic1_items:
    count +=i
print(count)

##############################################################
dic1 =  {'a':400, 'b':200, 'c':600}

dic1_items = dic1.values()
cnt = 0
for i in dic1:
    cnt =cnt + dic1[i]
print(cnt)