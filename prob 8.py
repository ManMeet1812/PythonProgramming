def swaplist(lst):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst


try:
    num = int(input("Enter number of elements you want in a list: "))
    
    if(num<2):
        print("WARNING!! Please enter sufficient number")
    else:
        print("Enter list elements:")
        lst = []
        for i in range(num):
            lt= int(input("Element:"))
            lst.append(lt)
        print("Entered list: ")
        print(lst)
    
        print("Enter the two positions number you want to swap in a list")
        pos1= int(input("Position 1: "))
        pos2= int(input("Position 2: "))
        print("Swaped list")
        print(swaplist(lst))
            
      
except ValueError:
    print("WARNING!! This is not a number!")
      
        
    
    
    
   

          
    