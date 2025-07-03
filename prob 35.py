print("Using Class")
class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(self.name +  " is a " + self.occupation)
        
a = Person()
#a.name = "Shuhbham"
#a.occupation =  "Accountant"
#print(a.name, a.occupation)
a.info()

print("Using Function")
def Person(a,b):
    print(a + " is a " + b)
    
Person("Shubham", "Accountant")