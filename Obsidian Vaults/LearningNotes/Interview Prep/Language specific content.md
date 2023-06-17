# Language specific content

Created: July 29, 2021 3:31 AM

### C++

Tip: Set in STL CAN NOT HANDLE PAIR<X,Y>. 

- Custom sort function writing format
    
    ```jsx
    sort(connections.begin(), connections.end(),
                [](const vector<int> &a, const vector<int> &b) {
                    return a[2] < b[2];
                });
    ```
    

### Python

1. Declaring a variable (eg. name) as _name means it is to be treated as private.
2. Dunders (__) around a method name mean the method is a magic method.
3. There are 3 method types: instance, class and static. Instance method can access attrs and methods on the same object and can access the class itself. Class method can access only class, not object instance. Static method can access neither.
4. In Python everything is passed to a function by reference. But it becomes pass by value if you completely change the data within the function. Example:

```jsx
# Definition 1
def fun(x):
    x[0] = 20

x = [10, 20]
print(fun(x)) # prints [20, 20]

# Definition 2
def fun(x):
    x = [30, 40]

x = [10, 20]
print(fun(x)) # prints [10, 20]

```

1. We can pass `args` to a function in Python to indicate variable number of arguments, and `*kwargs` to indicate keyword arguments (i.e. arguments that already have a name while passing into the function; we can iterate over them as dicts).
2. `ord('a')` will give ascii value of a; `chr()` converts ascii value to character.
3. Some more tips (GO THRU): 

[GitHub - chiphuyen/python-is-cool: Cool Python features for machine learning that I used to be too afraid to use. Will be updated as I have more time / learn more.](https://github.com/chiphuyen/python-is-cool)

1. Turns out max() is slower than if conditions.
- What is namespace? Types?
    
    the Python interpreter understands what exact method or variable one is trying to point to in the code, depending upon the namespace. When Python interpreter runs solely without any user-defined modules, methods, classes, etc. Some functions like print(), id() are always present, these are built-in namespaces. When a user creates a module, a global namespace gets created, later the creation of local functions creates the local namespace. The built-in namespace encompasses the global namespace and the global namespace encompasses the local namespace.
    
- Difference between * and **?
    
    "*" is used for packing/unpacking on lists and all. ** is used for dicts.
    
- List slicing creates copies.
- objects returned by map and filter are iterators, which means that their values aren't stored but generated as needed. After you've called sum(diffs), diffs becomes empty.
- reduce(fn, iterable, initializer) is used when we want to iteratively apply an operator to all elements in a list. For example, if we want to calculate the product of all elements in a list.
- Memoization in python?
    
    Via @lru_cache() or @cache in functools package. put this decorator in andd write normal recursive function