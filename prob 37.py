print(".....Check if the string is Palindrome or Symmetrical or Both.....")
strng = input("Enter string you want to check: ")

lststrng = list(strng)
print(lststrng)
a=len(strng)

if ((lststrng[0:a//2 ] == lststrng[a//2:]) and (lststrng[0: a//2] == lststrng[a//2-1 :: -1])):
    print(" Given string is symmetrical and palindrome")

elif (lststrng[0:a//2 ] == lststrng[a//2:]):
    print("Given string is symmetrical")
        
elif (lststrng[0: a//2] == lststrng[a//2-1 :: -1]):
     print("Given string is palindrome")

else:
     print("Given string is neither palindrome nor symmetrical")