def swaplist(lst):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst


try:
    num = int(input("Enter number of elements you want in a list: "))
    
        
except ValueError:
    print("WARNING!! This is not a number!")
    
print("Enter list elements:")

try:
    if(num<2):
        print("WARNING!! Please enter sufficient number")
    else:
        lst = []
        for i in range(num):
            lt= int(input("Elements:"))
            lst.append(lt)
        print("Entered list: ")
        print(lst)
    
except ValueError:
    print("WARNING!! This is not a number!")
    


try:
    print("Enter the two positions number you want to swap in a list")
    pos1= int(input("Position 1: "))
    pos2= int(input("Position 2: "))
      
except ValueError:
    print("WARNING!! This is not a number!")
      
        
    
    
    
print("Swaped list")    
print(swaplist(lst))
          
    