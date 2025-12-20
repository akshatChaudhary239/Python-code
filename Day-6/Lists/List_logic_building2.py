# Logic building on searching and  sorting 

# Linear searching - In this we search any element by comparing each element with the searched element
a = [10,20,0,40,50,60,70,80]
search = 99

for i in range(len(a)-1):
    if a[i] == search:
        print("found the element")
        break
else:
    print("No such element exist")  

# Binary searching -In this we divide the list into part for quick searching
a = [10,20,30,40,50,60,70,80,90,100]   
search = 80
start = 0
last = len(a)-1
mid = (start+last)//2
while start<=last:
    if a[mid]==search:
        print(f"element found on {mid}")
        break
    elif a[mid]<search:
        start = mid+1
        mid = (start+last)//2
    elif a[mid]>search:
        start = mid-1
        mid = (start+last)//2
else:
    print("no suhc element exist")      


# SORTING
# Bubble sorting - In this we sort the elements by swaping them based on their greater values
a = [23,44,22,52,225,322,224,2,42,14,23,54,23,55]

for j  in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i]>a[i+1]:
            a[i],a[i+1]= a[i+1],a[i]
print(a)        

# Selection sort
a = [23,44,22,52,225,322,224,2,42,14,23,54,23,55]
for i in range(len(a)-1):
    j = i+1
    min = i
    for k in range(j,len(a)):
        if a[k]<a[min]:
            min = k
    a[i],a[min] = a[min],a[i]
print(a)            