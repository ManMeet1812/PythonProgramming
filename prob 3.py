def swaplist(list):
    
    get = list[-1], list[0]
    list[0], list[-1] = get
    
    return list

newlist = [10,20, 15, 60]
print(swaplist(newlist))

    