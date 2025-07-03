a =1

try:
    b= int(input("Please Enter the Dividend: "))
    c=a/b
    print(c)

except ZeroDivisionError:
    print("Donot Enter Zero ")
    
except ValueError:
    print("Provide Number ")
    
except:
    print("something went Wrong ")
    
else:
    print("success")
    
finally:
    print("Processing Complete.")
    