# Question-1 take two input number and find which one is greater

Num1=int(input("enter a number"))
Num2=int(input("enter a number"))
if Num1>Num2:
    print("Num1 is greater")
else:
    print("Num2 is greater")    

# Question-2 greet the person on the basis of gender 

person1 = input("enter your gender")


if person1=="male" or person1 =="Male":
    print("hello sir grettings")
else:
    print("hello ma'am greetings")    
   
# Question-3 check the case senstivity of m,M,f,F 

gender = input("enter your gender")

if gender =="m" or gender=="M":
    print("hello sir")
elif gender =="f" or gender=="F":
    print("hello ma'am")
else:
    print("wrong gender")    

# Question-4 Even or odd checker

number = int(input("enter the number"))

if number%2==0:
    print("Even")
else:
    print("Odd")  
  
#  Question-5 voting eligibility

Age = int(input("enter your age")) 

if Age>=18:
    print("you are eligible for voting")
else:
    print(f'you are not eligible for voting you still have {18-Age} year to vote')    

# Question-6 Day number to Day name

Day_number = int(input("enter number from 1-7"))

if Day_number==1:
    print("sunday")
elif Day_number==2:
    print("Monday")    
elif Day_number==3:
    print("tuesday")    
elif Day_number==4:
    print("wednesday")    
elif Day_number==5:
    print("thursday")    
elif Day_number==6:
    print("friday")    
elif Day_number==7:
    print("saturday")   
else:
    print("please enter the valid day number")     

# Question-7 Greatest of three number

Num1 = float(input("enter the number"))
Num2 = float(input("enter the number"))
Num3 = float(input("enter the number"))

if Num1>Num2 and Num1>Num3:
    print("Num1 is the greatest number")
elif Num2>Num3 and Num2>Num3:
    print("Num2 is the greatest")
elif Num1==Num2 and Num1==Num3:
    print("All the number are equal ") 
elif Num1==Num2:
    print("Num1 and Num2 are equal")       
elif Num2==Num3:
    print("Num2 and Num3 are equal")       
elif Num3==Num1:
    print("Num3 and Num1 are equal")       
else:
    print("Num3 is the greatest") 

# Question-8 Check if it's leap year or not

Year= int(input("enter the year"))   

if Year%100==0 and Year%400==0:
    print("it's a leap year")
elif Year%100!=0 and Year%4==0:
    print("it's a leap year") 
else:
    print("it's a normal year")       

# Question-9 Shop discount calculator
price = int(input("enter the price of the item"))

if price>=1000 and price<=4999:
    print(f'your final price is {(price*90)/100}')
elif price>=5000:
    print(f'your final price is {(price*80)/100}')
else:
    print("no discount for you")        

# Question-10 vowel or consonant

letter= input("enter the letter")
if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
    print("it is a vowel")
elif letter=="A" or letter=="E" or letter=="I" or letter=="O" or letter=="U":
    print("it is a vowel")
else:
    print("it's a consonant")  

# using in

char= input("enter your letter")
if char in "aeiouAEIOU":
    print("it's a vowel")
else:
    print("it's a consonant")    


