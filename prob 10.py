# without Type Conversion
num1 = input("Enter first Num: ")
num2 = input("Enter second Num: ")

add= num1+num2
#prod= num1*num2

print(add)

# Type Conversion used

num1 = int(input("Enter first Num: "))
num2 = int(input("Enter second Num: "))

add= num1+num2
prod= num1*num2
div= num1/num2                 # Returns Floating Value
div2= num1//num2               # returns Integer Value

print(add, prod, div, div2)

x= 2
y=3
 
res= x+y
print(res)

y=9
res1= x+y
print(res1)

res2= +y
print(res2)
