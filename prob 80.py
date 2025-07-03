sink = ['bowl', 'plate', 'cup']

for dish in sink:
    print('Putting {} in the dishwasher'.format(dish))
    
################################################################
print(".........Look at this scenario..........")

sink = ['bowl', 'plate', 'cup']

for dish in sink:
    print('Putting {} in the dishwasher'.format(dish))
    sink.remove(dish)

##################################################################
print("\r")
    
print(".........Look at another scenario..........")

sink = ['bowl', 'plate', 'cup']

for dish in list(sink):   #####list(sink) create copy of the list
    print('Putting {} in the dishwasher'.format(dish))
    sink.remove(dish)