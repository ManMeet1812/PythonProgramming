try:
    a=int(input("Enter first element: "))
    b=int(input("Enter seocnd element: "))

    if a>b:
        print("Maximum element is: ", a)
    else:
        print("Maximum element is: ", b)
        
except ValueError:
         print("WARNING! Not an Integer!!")
         
# 2 Method
        
a=int(input("Enter first element: "))
b=int(input("Enter seocnd element: "))

c= max(a,b)
print("Maximum element is: ", c)

# 3 Method
a=int(input("Enter first element: "))
b=int(input("Enter seocnd element: "))
print("Maximum element is: ")
print(a if a>=b else b)

# 4 Method
a=int(input("Enter first element: "))
b=int(input("Enter seocnd element: "))
mx1 = lambda a,b:a if a>b else b
print("Maximum element is: ", mx1)
print(f"Maximum{a,b} is the maximum element is: ")
print(f'{mx1(a,b)} is the maximum element' )

# 5 Method
a=int(input("Enter first element: "))
b=int(input("Enter seocnd element: "))
x= [a if a>b else b]
print("Maximum element is: ", x)

# 6 Method
a=int(input("Enter first element: "))
b=int(input("Enter seocnd element: "))
x= [a,b]
x.sort()
print("Maximum element is: ", x[-1])



        