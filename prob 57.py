test_tup = (5, 20, 3, 7, 6, 8)

test_tup = list(sorted(test_tup))
res=[]
k=1
for i, x in enumerate(test_tup):
    if i<k or i>=len(test_tup)-k:
        res.append(x)
print(tuple(res))

#######################################################
tup = (5, 45, 67, 70, 15, 25)

tup = sorted(tup)
k=2
print("Minimum 2 elements: ", tup[:k])
print("Maximum 2 elements: ", tup[len(tup)-k:])

########################################################
import heapq
test_tup = (10, 54, 35, 78, 3)
k = 2
smallest = heapq.nsmallest(k, test_tup)
largest = heapq.nlargest(k, test_tup)
print(smallest, largest)

#######################################################
tup1 = (1, 54, 35, 7, 3, 100, 45)
tup1 = list(tup1)
min1 =[]
max1 =[]
k=2
i=0

while i<k:
    min1.append(min(tup1))
    tup1.remove(min(tup1))
    i=i+1

i = 0
while i<k:
    max1.append(max(tup1))
    tup1.remove(max(tup1))
    i=i+1

res= min1+max1
print(res)


