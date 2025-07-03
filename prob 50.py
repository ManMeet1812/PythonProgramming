string = "geeks quiz practice code"
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))


################################################################

def rev_string(strng1):
    words = strng1.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence

strng = "geeks quiz practice code"
print(rev_string(strng))

###############################################################

import re

def rev_Strng(sentence):
    words = re.findall('\w+', sentence)
    reverse_sentence = ' '.join(words[i] for i in range(len(words)-1, -1, -1))
    return reverse_sentence

input = "geeks quiz practice code"
print(rev_Strng(input))


