strng = 'amaama'
half = int(len(strng))

first_strng = strng[:half]
second_strng = strng[half:]

#Symmetric
if(first_strng == second_strng):
    print("The Given string is Symmetric")
else:
     print("The Given string is not Symmetric")
     
if(first_strng == second_strng[::-1]):
    print("The Given string is Palindrome")
else:
     print("The Given string is not Palindrome")