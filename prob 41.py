def split_string(string):
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    string = '-'.join(list_string)
    return string

string = 'Geeks for Geeks'
list_string = split_string(string)
print(list_string)

new_string = join_string(list_string)
print(new_string)

##############################################################
s = 'Geeks for Geeks'
print(s.split(" "))
print('-'.join(s.split()))

###########################################
