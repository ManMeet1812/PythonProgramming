def Remove(st):
    while(st):
        st.pop()
        print(st)

st = {71, 25, 65, 80, 75}
Remove(st)


#########################################################
myset= {23, 43, 12, 67, 41}

while(myset):
    myset.discard(max(myset))
    print(myset)
    
########################################################
my_set = set([12, 10, 13, 15, 8, 9])

for i in range(len(my_set)):
    myset.remove(next(iter(my_set)))
    print(my_set)
