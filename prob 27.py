#lst = ['Harsh', 'weds', 'Manmeet', 'on', 30 , 'January', 2023]
#new_lst=[]

ab=int(input("Enter length of elements: "))
abc = []
for i in range(ab):
    lstele = input("Elements"+ str(i+1) + ": ")
    abc.append(lstele)
print(abc)

# using while loop
ab=int(input("Enter length of elements: "))
abc = []
i=0
while(i<=ab):
    lstele = input("Elements"+ str(i+1) + ": ")
    abc.append(lstele)
    i= i+1
print(abc)

