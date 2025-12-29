# we use this to perform crud operations 
# we use open() to define any file name or define any path
# to read - file_name.read()  
#to write - open("file_name",'w')
# to append -  open("file_name",'a')
# to create a file we use 'x'

# using 'with'
# with - it helps us to close the file automatically
with open("file_name",'r') as fs:
    print(file_name.read())