# FUNCTIONS
# functions are a block of code which we can call again and again to perform any task 

# example
def hello():
    print("Hello there this is python language")

hello()    #we are calling our function

# print vs return
# return takes the output or anything we want to return to where the function is called

def name():
    return "my name - Akku"

# name() # here the return has taken the desired output to name() but we can't print it because return can't print anything
# so in order to print it we can either print it directly or by storing it in a variable
# VARIABLE-
copy_name = name()
print(copy_name) 
# or directly
print(name())



# parameters
def sum(a,b):
    print(a+b)
sum(5,8)

# finding a palindrom using function

def palindrom(a):
    copy = a
    rev = 0
    while a>0:
        rev = (rev*10) + (a%10)
        a = a//10
    if rev==copy:
        return True
    else:
        return False

number_1 = int(input("enter a number"))                
number_2 = int(input("enter a number"))                
number_3 = int(input("enter a number"))                
number_4 = int(input("enter a number"))  

print(palindrom(number_1))
print(palindrom(number_2))
print(palindrom(number_3))
print(palindrom(number_4))




       
        








