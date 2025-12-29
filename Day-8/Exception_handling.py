# exception handling
# exceptions are raised when their is no ysntax error but the result still gets some error this doesn't stop the program but changes the flow of the program

a = int(input("enter a number "))
b = int(input("enter a number "))

try:
    print(a/b)
except Exception as error:
    print(error)    

print(a+b)    

# else - we can use else with try and except too
c = int(input("enter a number "))
d = int(input("enter a number "))

try:
    print(c/d)
except Exception as error:
    print(error)  
else:
    print("correct numbers for division")      

print(c+d)  

# finally - it will execute no matter what

e = int(input("enter a number "))
f = int(input("enter a number "))
try:
    print(e/f)
except Exception as e:
    print(e)    
finally:
    print("i will be printed no matter what")    


# Raise - we use to make custom errors warning

age = int(input("enter eyour age "))
try:
    if age<18:
        raise Exception("you must be 18+")
    print("Access granted")
except Exception as e:
    print(e)        
