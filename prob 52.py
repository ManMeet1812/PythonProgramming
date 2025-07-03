strng = 'czsfdgbfhfjgyj'
print(len(strng))

for i,x in enumerate(strng):
    pass
print(i+1)

############################################

def findlen(str1):
    counter= 0
    for i in str1:
        counter +=1
    return counter

strn = 'ascsdvfsv'
print(findlen(strn))

#############################################

def find_len(str2):
    counter = 0
    while(str2[counter:]):
        counter +=1
    return counter

str2 = 'sfsdgsfsdgddgdg'
print(find_len(str2))


##############################################

import functools

def findlen(string):
    return functools.reduce(lambda x,y: x+1, string, 0)

string = 'geeks'
print(findlen(string))

####################################################
def findlen(str3):
    return sum(1 for i in str3)

string = 'manmeetlovesharsh'
print(findlen(string))
    