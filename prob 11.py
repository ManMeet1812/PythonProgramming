import re

y= "My name is Manmeet Kaur. I am married to Harshdeep Singh."

pattern= "Harshdeep Singh."


x= re.search(pattern, y)

if x:
    print("Match Found!!")
    
else:
     print("Match Not Found")
     
     
a = "Hello! Michael Jackson has: 12 characters."
print(a)
res= a.replace('Michael','Janet')
print(res)

upp= a.upper()
print(upp)