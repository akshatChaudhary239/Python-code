# WHILE LOOPS
# while loop keeps iterating until it reaches it's false condition
# As long as the condition is true the loop will keep iterating

a = 10
while a>0:
    print(a)
    a -= 1

# BREAK
#  breaks the loops when the condition is met
a = 1
while a<=10:
    print(a)
    a +=1
    if a == 6:
        break

# CONTINUE
# it breaks only one iteration in a loop and conitnues to print all the other interation
a = 0
while a <=10:
    a +=1
    if a == 6:
        continue
    print (a)

# ELSE
# if a break keyword is encountered then the else keyword will not work and if no break keyword encountered then else will work

for i in range(1,6):
    if i ==7:
        break
    print(i)
else:
    print("No Break to Encounter")