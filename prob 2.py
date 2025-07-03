def swaplist(newlist):
    newlist[0], newlist[-1] = newlist[-1], newlist[0]
    return newlist
newlist = [10,20, 15, 60]
print(swaplist(newlist))
