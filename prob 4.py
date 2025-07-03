def swaplist(lst):
    if len(lst) >= 2:
        lst = lst[-1:] + lst[1:-1] + lst[:1]
        
    return lst

inp=[12, 35, 9, 56, 24]
print(swaplist(inp))
    

        
    
        