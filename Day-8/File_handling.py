# exception handling
# exceptions are raised when their is no ysntax error but the result still gets some error this doesn't stop the program but changes the flow of the program

a = int(input("enter a number "))
b = int(input("enter a number "))

try:
    print(a/b)
except Exception as error:
    print(error)    

print(a+b)    