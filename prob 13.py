def swplst(lst):
    #swaplst = []
    get=lst[0],lst[3]
    lst[3], lst[0]= get
    return(lst)


try:
  ln = int(input("Enter length of the list: "))
  if ln<=1:
      print("WARNING!!! PLEASE ENTER SUFFICIENT NUMBER")
  else:
      print("Enter elements for the list: ")

      lst = []
 
      for i in range(ln):
         a=int(input("Element: "))
         lst.append(a)
      print(lst)
      print(swplst(lst))
      
      
      
except ValueError:
    print("Warning!!! This is not a Number")