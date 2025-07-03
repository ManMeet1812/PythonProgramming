try:
    num = int(input("Enter number of elements you want in a list: "))
    
except ValueError:
    print("WARNING!! This is not a number!")
    
print("Enter list elements:")

try:
    lst = []
    for i in range(num):
        lt= int(input("Elements:"))
        lst.append(lt)
    print(lst)
    
except ValueError:
    print("WARNING!! This is not a number!")
          
    