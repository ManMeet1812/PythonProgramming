tup = (23, 45, 76, 89, 90)
print("Size: ", len(tup))
 
 ##########################
counter =0
for i in tup:  
    counter+= 1
print(counter)

################################
def find_tup_len(tup):
    counter = 0
    while(tup[counter:]):
        counter += 1
    print(counter)
    
find_tup_len(tup)

###############################
print(sum(1 for i in tup))
