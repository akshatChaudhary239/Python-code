# Logic building questions

# count the frequency of the array
a = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5]
d = {}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i] = 1 

print(d)    

# check if two strings have same frequency map
a = "aabbcc"
b = "babacc"

if len(a)==len(b):
    d={}
    for i in a:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for i in b:
        if i in d.keys():
            d[i]-=1
        else:
            print("your elements are not same")
    for i in d:
        if d[i]!=0:
            print("not same elements")   
            break
    else:
        print("your strings are same")
else:
    print("not same strings")                         
 
        
# Check if all characters of one string exist in another

a="akkubhaisahabh"
b="akkubhaisahabhjikijai"
d = {}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for i in b:
    if i in d.keys():
        d[i]-=1
    else:
        print("String is not same") 
for i in d:
    if d[i]!=0:
        print("Not same string")    
        break
    else: 
        print("your string is same")          


# Find the unique element in a list
a=[1,1,1,1,1,2,2,2,2,23,3,3,3,3,4,4,4,4,5,5,5,5,]
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
unqiue = 0  
for i in d:      
    if d[i] <= 1:
        print(i)

# Intersection of 2 Arrays
a=[1,2,3,4,5,6]
b=[2,3,4,1,7,8]
j = []
d={}
for i in a:
    if i in d.keys():
        d[i]==1
    else:
        d[i]=1
for i in d.keys():
    if i in b:
        j.append(i)
print(j)                  
           