Python tips
- Declaring a variable (eg. name) as _name means it is to be treated as private.
- Dunders (__) around a method name mean the method is a magic method.
- There are 3 method types: instance, class and static. Instance method can access attrs and methods on the same object and can access the class itself. Class method can access only class, not object instance. Static method can access neither.
- In Python everything is passed to a function by reference. But it becomes pass by value if you completely change the data within the function.
ex:
```
def fun(x):
    x[0] = 20

x = [10, 20]
print(fun(x)) # prints [20, 20]
```
```
def fun(x):
    x = [30, 40]

x = [10, 20]
print(fun(x)) # prints [10, 20]
```
- We can pass ```*args``` to a function in Python to indicate variable number of arguments, and ```**kwargs``` to indicate keyword arguments (i.e. arguments that already have a name while passing into the function; we can iterate over them as dicts).
- ord('a') will give ascii value of a; chr() converts ascii value to character.