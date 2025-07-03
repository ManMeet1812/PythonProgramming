def swaplist(newlist):
    size= len(newlist)
    
    temp = newlist[0]
    newlist[0] = newlist[size -1]
    newlist[size -1] = temp
    
    return newlist

newlist = [10, 25, 15, 21, 8]
print(swaplist(newlist))

    