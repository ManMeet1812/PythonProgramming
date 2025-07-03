strng = "GeeksforGeeks "
lt =  ''

for i in range(len(strng)):
    if i != 2:
        lt = lt+strng[i]
print(lt)


strng = "GeeksforGeeks "
# Printing string after removal
# removes all occurrences of 'e'
new_strng = strng.replace('e', '')
print(new_strng)

new_strng1 = strng.replace('e', '',1)
print(new_strng1)


new_strng2 = strng[:2] + strng[3:]
print(new_strng2)

new_strng6 = ''.join(strng[i] for i in range(len(strng)) if i!= 4)
print(new_strng6)

str = 'Geeks123For123Geeks'
print(str.translate({ord(i): None for i in '123'}))


def remove_char(s, i):
    b = bytearray(s, 'utf-8')
    del b[i]
    return b.decode()
 
# Example usage
s = "hello world"
i = 4
s = remove_char(s, i)
print(s)