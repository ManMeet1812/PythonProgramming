test_string = 'ManmeetLovesHarsh'
print("The Original String: " + test_string)

print(list(reversed(test_string)))

res= ''.join(reversed(test_string))
print("The Reversed String: " +res)

##################################################
test_string = "istudyfromgeeksforgeeks"
print("The Original String: " + test_string)
a = len(test_string)

res = test_string[(a-1) :: -1]
print("The Reversed String: " +res)

##################################################
print("################################################ ")
test_string = "geeksforgeeks"
print("The Original String: " + test_string)
a = len(test_string)
ans = test_string[::-1]
print(ans)

ans1 = test_string[::-1][a-1:]
print(ans1)

ans2 = test_string[:a]
print(ans2)

ans3 = test_string[:a][::-1]
print(ans3)