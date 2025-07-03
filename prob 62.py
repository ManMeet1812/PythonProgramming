def dictionary():
    key_value = {}
    key_value[2] = 54
    key_value[5] = 4
    key_value[3] = 34
    key_value[7] = 20
    key_value[8] = 5
    key_value[1] = 12
    key_value[4] = 45
    
    print("Key Value", key_value)
    print("Sorted Key")
    
    for i in sorted(key_value.keys()):
        print(i, end = ': ')
        print(key_value[i], end = ', ')
        
dictionary()