# Numpy/Scipy/Pandas

Created: November 10, 2021 7:08 PM

Numpy

- Why are loops slow in Python?
    
    Because it is a dynamically typed language. It doesn't know what data type the loop object is, so no optimizations possible.
    
- What is vectorization?
    
    the term vectorization of a function means that the function is now applied simultaneously over many values instead of a single value
    
- What is the rank of a Numpy matrix?
    
    Number of dimensions it has. Eg - matrix of size(3,4) has dim 2.
    
- Important random functions
    
    Shuffle data: `np.random.shuffle(data)`
    
    Random sampling: `random.sample(range(data.shape[0]), 4)`
    
- What is memory representation of numpy ndarray?
    
    row major
    
- Always remember (read)
    
    Axis = 0 is across ROWS (top to down). Axis = 1 is across COLUMNS (left to right).
    

Pandas

- Two data structures it offers?
    
    Series and Dataframe
    

[https://github.com/guipsamora/pandas_exercises](https://github.com/guipsamora/pandas_exercises)