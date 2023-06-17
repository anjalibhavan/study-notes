# Perceptron

- What is the difference between feed-forward NNs and perceptrons?
    
    Perceptrons don’t have activation functions.
    
- What is a perceptron?
    
    Very simple algorithm which is “online” (meaning it processes one example at a time). Labels are +1 and -1. Basically loops MAXITER times, then in each loop loops over each training sample, calculates $a = w^{T}x + b$, multiplies it with true label to see if it is greater than 0. If yes, then both have the same sign so correct prediction. Else wrong. If correct, do nothing. If wrong, update weights and biases. Continue!
    
- Decision boundary for perceptron?
    
    In D dimensional space, it is always a D − 1-dimensional hyperplane.
    
- Pros and cons of perceptron?
    
    Online algo so very simple and effective. Data needs to be linearly separable. It can only have linear decision boundaries. Cannot handle problems like XOR.
    
- Assumptions underlying perceptron?
    
    The assumptions the Perceptron makes is that data is linearly separable and the classification problem is binary.
    

Neural networks basically combine multiple perceptrons and give non-linear decision boundaries.