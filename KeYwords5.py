a = 10    #initializing variable globally

# used to read the variable
def read():
    print(a)

# changing the value of globally defined variable
def mod1():
    global a
    a=5

# changing value of only local variable
def mod2():
    a = 15
# reading initial value of a
# prints 10
read()

# calling mod 1 function to modify value
# modifies value of global a to 5
mod1()

# reading modified value
# prints 5
read()

# calling mod 2 function to modify value
# modifies value of local a to 15, doesn't effect global value
mod2()

# reading modified value
# again prints 5
read()