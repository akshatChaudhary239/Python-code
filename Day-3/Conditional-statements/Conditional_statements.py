# if, elif and else statements

# if else statement example

Password = input("please enter the password")
if Password=="akku1234":
    print("Acces Granted")
else:
    print("Access Denied")  

# if elif else statement example 

Money = int(input("how much money you want 10,20,30,40"))

if Money<=10:
    print("i can buy a toffee")
elif Money==20:
    print("i can now buy a pen")
elif Money==30:
    print("i can now buy a pen and a toffee")     
elif Money==40:
    print("i can buy a meal")
else:
    print("i can buy a meal and a pen")        


# if elif else with logical operators

Salary1 = int(input("enter your salary"))
Salary2 = int(input("enter your salary"))
Salary3 = int(input("enter your salary"))


if Salary1>Salary2 and Salary1>Salary3:
    print("salary1 is the highest")
elif Salary2>Salary1 and Salary2>Salary3:
    print("salary2 is the highest")
else:
    print("salary3 is the highest")    


