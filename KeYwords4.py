#global: This keyword is used to define a variable inside the function to be of a global scope.
#non-local : This keyword works similar to the global, but rather than global, this keyword declares a
#variable to point to variable of outside enclosing function, in case of nested functions.
a= 15
b= 10

def add():
    c= a+b
    print(c)

add()

def fun():
    var1 = 10
    
    def gun():
        nonlocal var1
        
        var1 = var1+a
        print(var1)
        
        
    gun()
    
fun()