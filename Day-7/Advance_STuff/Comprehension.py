# Lambda expression
# we can use a lmbda expression for small equation probelms in one line

add = lambda x,y:x+y
print(add(12,12))

# Map - If we have to apply a function on all the values of a list then we use map
a = [1,2,3,4,5,6]
l = map(lambda x: x**2,a)
print(list(l))

# Or
a = [1,2,3,4,5,6]
def square(x):
    return x**2
l = map(square,a)
print(list(l))

# Filter - we use it to filter out things

# fitering out even numbers
a = [1,2,3,4,5,6]
l = filter(lambda x:x%2==0,a)
print(list(l))

# zip - we use it to combine different elements/lists into one
a = ["akku","akshat","super"]
age = [19,20,23]
l = zip(a,age)
print(dict(list(l)))


# Comprehensions - it is a way of writing our code in one line

# List comprehension - 
a = [1,2,3,4,5,6,7,8,9]
l = [i for i in a if i%2==0]
print(l)

# Set comprehension - 
a = [1,2,3,4,5,6,7,8,9]
l = {i for i in a if i%2==0}
print(l)


# List comprehension - 
a = [1,2,3,4,5,6,7,8,9]
l = {i:i**2 for i in a if i%2==0}
print(l)     #main difference is of brackets


# Generators - they are used when we have to generate anything or any element
def gen():
    for i in range(5):
        yield i
generator = gen()        
print(next(generator))       # we use yield and next in generators

# Decorators