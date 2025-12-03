# # Logical operator
# # and , or , not

# # Example of and
# print(23==34 and 45==45 and 44==34 and 34==34) #All the conditions must be true to get true in the result

# # Example of or
# print(23==34 or 45==65 or 66==66) # It will give true becuase one condition is true 

# # Example of not
# print(not 23==23, not 34==34, not 44==44)


candies =int(input("enter the number of candies"))
kids = int(input("enter the number of kids"))
candies_per_kid = candies//kids
Remaining_candies = candies%kids
print(f"""
Candies per kid: {candies_per_kid}
Remaining_candies: {Remaining_candies}
""")