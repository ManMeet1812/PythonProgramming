def swplst(lst):
    swaplst = []
    for i in range(ln+1):
         swaplst.append(lst[-i])
    print(swaplst[1:])
    

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
      swplst(lst)
      
      
      
except ValueError:
    print("Warning!!! This is not a Number")
