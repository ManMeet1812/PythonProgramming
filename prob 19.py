a = 19
b = 12

if a<b:
    print(f"{a} is minimum")
else:
    print(f"{b} is minimum")
    
# 2nd method
a=38
b=100

c= min(a,b)
print(c," is minimum" )

# 3rd method
a=45
b=65
print("minimum value is:", sorted([a,b])[0])

#4th method
from functools import reduce

a=49
b=50
c=reduce(lambda a,b:a if a<b else b, [a, b])
print(c)