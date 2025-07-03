def fact_iterative(num):
    fac = 1
    for i in range(num):
        fac = fac*(i+1)
        
    print(fac)
    
fact_iterative(5)

###############################################################
def fact_recursive(num):
    if num == 1:
        return 1
    else:
        return num*fact_recursive(num-1)

print(fact_recursive(5))