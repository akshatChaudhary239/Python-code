# break the digits and print digits in reverse order
 
# a = 1234

# while a>0:
#     print(a%10, end=" ")
#     a = a//10

#  SUM OF DIGITS

# a = int(input("enter a number "))
# s = 0
# while a > 0 :
#     s = s+a%10
#     a = a//10
# print(s)  

# reverse a digit
# a = int(input("Enter a number "))
# rev = 0
# while a > 0:
#     rev = rev*10 + a%10
#     a = a//10
# print(rev)  

# Palindrome number
# a = int(input("enter a number"))
# copy = a
# rev = 0
# while a >0:
#     rev = rev*10+a%10
#     a = a//10


# print("the number your entered",copy)
# print("the reverse of the number your entered",rev)
# if rev == copy:
#     print("your number is a palindrome number")
# else:
#     print("your number is not a palindrome number") 


# Automorphic number
# a = 25
# copy = a
# square = a**2
# count = 0
# while a>0:
#     count  = count+1
#     a = a//10 
 
# extract = square % (10**count)

# if extract == copy:
#     print("your number is automorphic")
# else:
#     print("your number is not automorphic")    

