# print "Hello world" n times
Number = int(input("enter the numberr of times you want to print hello"))
for hello in range(Number):
    print("hello world")

# print numbers from 1 to n
Number = int(input("enter a number"))
for i in range(1,Number+1):
    print(i)

# print number from n to 1
Number = int(input("enter a number "))
for times in range(Number,1,-1):
    print(times)

# print the sum of the natural number from 1 to n
Number = int(input("enter a number"))
sum = 0
for times in range(1,Number+1):
    sum = sum+times
print(sum)  


# factorial of an number n

number = int(input("enter a number"))
factorial = 1
for i in range(1,number+1):
    factorial = factorial*number

print(factorial) 

# find the sum of n even and n odd numbers separately

even = int(input("enter an even number"))
odd = int(input("enter an odd number"))

eve = 0
od = 0

for i in range(0,even,2):
    eve = eve+i
for i in range(1,odd,2):
    od = od+i    

print(eve)
print(od)  

# second way

Number = int(input("enter a number"))
even_sum = 0
odd_sum = 0
for i in range(0,Number+1):
    if i%2==0:
        even_sum += i
        
    else:
        odd_sum +=i   
       
print(even_sum)
print(odd_sum)

# Display all the numbers that divide the n number completely

Number = int(input("enter a number"))   
for i in range(1,Number+1):
    if Number%i == 0:
        print(i)   

# Sum of all factors
Number = int(input("enter a number "))
sum = 0 
for i in range(1,Number+1):
    if Number%i==0:
        sum = sum+i
print(sum)       

# Power calculation
Number = int(input("enter a number"))
Number_2 = int(input("enter a number"))
Power = Number
for i in range(Number_2-1):
    Power = Power*Number

print(Power)



# Prime number check , check if it is divisible by only 1 and itself

number = int(input("enter a number "))

count = 0 
for i in range(1,number+1):
    if number%i==0:
        count+=1

if count ==1:
    print("it is a unity number")
elif count==2:
    print("it is a prime number")                
else:
    print("it is a composite number")    