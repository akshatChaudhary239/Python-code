# Lists logic building questions

# Sum and average of list

a = [10,20,30,40,50]
sum = 0
for i in a:
    sum = sum+i
print(sum) #sum
print(sum/len(a))  #average

# Maximum element with index

b = [100,102,201,203,400]

max = b[0]
for i in range(len(b)):
    if b[i]>max:
        max = b[i]
        index = i 
print(max)    
print(index)

# Second greatest element
li = [20,20,36,4,62,56,35,77]
frst_element = li[0]
secnd_element= li[0]

for i in range(len(li)):
    if li[i]>frst_element:
        secnd_element= frst_element
        frst_element = li[i]
print(secnd_element)        


# check whether the list is sorted in ascending order or not
a = [12,56,34,67,24,67,35,88,22]

max = a[0]
for i in range(len(a)-1):
    if a[i]<a[i-1]:
        continue
    else:
        print("your list is not sorted")
        break

else:
    print("your list is sorted ")

# Shift all the positions to left by 1 and move the first position to the last

a = [10,20,30,40,50,60,70]
for i in range(len(a)-1):
    a[i+1],a[i] = a[i],a[i+1]
print(a)    

# Shift all the positions to right by 1 and move the last position to the first

a = [10,20,30,40,50,60,70]
for i in range(len(a)-1,0,-1):
    a[i],a[i-1] = a[i-1],a[i]
print(a)    
        
# Make the rotation work k number of time

k = int(input("enter a number "))

a = [10,20,30,40,50,60,70]
for i in range(k):
    for i in range(len(a)-1):
        a[i],a[i+1]= a[i+1],a[i]

print(a)        

# Reverse the entire list(without using swap)
a = [10,20,30,40,50,60,70,80]
b = len(a)-1
for i in range(len(a)//2):
    a[i], a[b] = a[b],a[i]
    b = b-1
print(a)    
