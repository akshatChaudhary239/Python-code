#CHAPTER-1
val1 = int(input("enter your age : "))
val2 = int(input("enter your age : "))
print("your answer is", val1+val2)

# print area of a square

# first we will take the side of a square because a squares's all sides are equal
side = int(input("enter the side "))
Area = side*side
print("you answer is" , Area)

# Write a program to input 2 float numbers and print their average
val1 = float(input("enter your first number : "))
val2 = float(input("enter your second number : "))
Average = (val1+val2) / 2
print("your answer is ",Average)


#CHAPTER-2
# Strings and conditional statements
val1 = "akku chaudhary"
print(val1[0:])
# take a input form the user and print its length
val1 = str(input("enter your character : "))
print(val1.count("$"))
# check if the number enterred by user is odd or even

num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))
 
if(num1>num2 and num1>num3):
    print("numer one is the greatest ")
elif(num2>num1 and num2>num3):
    print("Number two is the greatest")
else:
    print("number three is the greatest")    

# PYTHON QUESTIONS :-


#CHAPTER-3
#Tuple anbd lists

val1 = ["akshat", 20, 6.1 , "Sonipat"]
print(val1[0])
val1[0]="akku"
print(val1)

#LIST.APPEND  (it adds a element in the end of the list)
val1 = [1,2,3,4]
val1.append(5)
print(val1)

#LIST.SORT (it sorts the list in ascending order)
val1 = [3,2,5,6,1]
val1.sort()
print(val1)

#LIST.SORT(RESERVE=TRUE) (it sorts the list in descending order)
val1 = [5,3,4,6,8,9]
val1.sort(reverse=True)
print(val1)

#LIST.REVERSE (it reserve the list)
val1 = [3,4,5,6,7,8]
val1.reverse()
print(val1)

#LIST.INSERT(idx,value) (idx ka mtlb hai index mtlb 0,1,2,3 wala and value mtln ki humne assigned index prr konsi value rakhni hai)

val1 = [1,2,3,4,5]
val1.insert(1,8)
print(val1)

#LIST.REMOVE()  (removes the element written in the parameter , or we can remove the first element out of many other same multiple elements)

val1 = [2,1,3,1,4,5,6]
val1.remove(1)
print(val1)

#LIST.POP(IDX)  (removes the element based on the index address)
val1 =  [1,2,3,4,5,6]
val1.pop(0)
print(val1)

#TUPEL (tupel is nothing but a built in data type in oython which ets us build immutable squences of values)
 # (tupel is just like list bss isne square bracket in jagah function brackets lgti hai)
# print(val)

#wap to ask the user to enter names of their three fav movies and stre it in a list

movie1 = str(input("Enter your fav movie"))
movie2 = str(input("Enter your fav movie"))
movie3 = str(input("Enter your fav movie"))
 
favs= [movie1,movie2,movie3]
print(favs)


#CHAPTER-4 (DICTIONARY AND SETS)

person1 = {
    "name": "akku",
    "rollno": 22991,
    "personality" :"mast",
    "feature" : ["acha insaan", "good listener"]
}
person2 = {
    name: "vansh",
    rollno: 22993,
    personality :"good",
    feature : ["only insaan", "average listener"]
}
person3 = {
    name: "rohit",
    rollno: 22995,
    personality :"average",
    feature : ["acha banda", "ok listener"]
}
print(person1["feature"])

#Dictionary methods
person1.keys() # to get all the keys in our dictionary
person1.get("value") # to get the specific value in our dictionary
person1.values()  #to get all the values in our dictionary
person1.items() # returns all  the keys and values of our dictionary
person1.update()  #we can add any new value in our dictionary

#SETS 
#set is the collection of unordered items, it ignores multiple repeated items in a set
set2 = {1,2,3,4,1,2,2,2,2 , "hello", "heelo" , "hello"}
print(set2)

set2 = set() #it is an empty set

#sets methods
set2.add()# we can add tuple for adding miltiple values at one time but not list
set2.remove()# we use it to remove any element
set2.clear()# we use it to clear the full set
set2.pop() #to remove an random element
set2 = {1,2,3,2,3,1,2 , "hello", "world","hello"}
set2.add((5,6,7,8,9))
print(set2)
set1= {1,2,3}
set2= {1,3,4,5}

# print(set1.union(set2)) it ignore the  duplicate items write it one time and prints all the elements of the sets
# print(set1.intersection(set2)) prints only the common items of two sets

#LOOPS

#while loop (if  we want to print or get something until the definedd condition we use while loops)

count = 1
while count <= 5 :
    print("hello this is me")
    count = count+1

#print number from 1 to 100

count= 1
while count<=100 :
    print("number",count)
    count += 1  #count ko hmesha iss syntax se badhana yaa ghatana hai

#print number from 100 - 1 

count = 100
while count >= 1 : 
    print("hello",count)
    count -= 1

# print multiplication table of a n number

num = int (input('enter your number : '))

i = 0
while(i<=10):
    print(num* i)
    i +=1

#finding an number from a list
num = (1,2,3,4,5,6,7,8,9)
x = 5
i = 0 
while i < len(num):
    if num[i] == x:
       print('found your number at', i )
       break
    i += 1
else:
        print("still searching")
        
print("end of loop")


# print even odd with the help of continue 
i = 1
while(i<=10):      #iss code me agar(if) i hai voh 2 ka module hai toh usse skip krdo continue function  chize  skip krta hai jousko condition de rkhi hoti hai orcondition ko skip kraake code ko aage run kraadeta hai whereas break jo hai voh voh condition true hone prr code ko rok deta hai
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1


#FOR LOOP

listt = (1,4,9,16,36,14,6,8,9)

x = 16
idx = 0
for vals in listt:
    if(vals == x):
        print("found the element", idx)
    idx += 1

# RANGE
for i in range(2,10,2):  #(start,stop,step)
    print(i)

#print numbers from 1 to 100

num = int(input("enter a number : "))
for i in range(1,11,):
    print(num*i)

# print the sum of n natural numbers

num = 5

sum = 0
for i in range(1,num+1):
    sum += i
    
print(sum)

#write a program to find the factorial of first n numbers (using for)
num = 5
fact = 1 
i = 1
while i <=num:
    fact *= i 
    i +=1
print(fact)

#CHAPTER-6  FUNCTIONS AND RECURSION 
def calsum(a,b):
    print(a+b)
    return

calsum(1,2)
calsum(3,2)

#OBJECTS

class Car:
    def __init__(self, Price) :
        self.value= Price

c1=Car(100)
print(c1.value)

class Car:
    def __init__(self,price):
        self.number=price
    def method(self):
        print("hello thess are your marks")  


c1= Car(100000)
print(c1.number)
c1.method()

# create a class that takes names and marks of 3 students and also create a method to print the average

class Student:
    def __init__(self,fullname, marks):

        self.name= fullname
        self.number = marks

    def average(self):
        sum = 0
        for val in self.number :
            sum+= val
            print("hello",self.name, "this is your avg score",sum/4)  


s1 = Student("Akshat",[97,97,97,97])
  
s1.average()

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

ac1 = Account("12234543","121313")
print(ac1.acc_no)
print(ac1.acc_pass)
  