def fun():
    print("Inside Function")
    
fun()

def func():
    s=0
    for i in range(10):
        s+=i
        
        return s
print("return function")   
print(func())

#yield : This keyword is used like return statement but is used to return a generator.

def func():
    s=0
    for i in range(10):
        s+=i
        
        yield s
print("yield function")
for i in func():
    print(i)
    
#Lambda keyword is used to make inline returning functions with no statements allowed internally.     
g = lambda x: x*x*x
print("lambda function") 
print(g(6))
