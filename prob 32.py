def printAll(*args):
    print("No. of arguments: ", len(args))
    for i in args:
        print(i)
        
printAll('Manmeet','kaur', 'Harshdeep','Singh')
printAll('jasson','japman','singh')

#######################
def printDictionary(**args):
    for key in args:
        print(key + ":" + args[key])
        
printDictionary(Countary = 'Canada', Province = 'Ontario', City='Brampton')
        