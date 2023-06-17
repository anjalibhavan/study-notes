# SVM

- Why does SVM look for a decision boundary that's far away from data points?
    
    Because points closer to the boundary lead to uncertain classifications.
    
- What is a decision hyperplane?
    
    A decision hyperplane divides the data points into decisions. It is defined by the intercept term $b$ and a normal vector $\vec{w}$ perpendicular to the plane.
    
- What are support vectors?
    
    SVs are small subsets of the data that fully specify the SVM decision function.
    
- What is a geometric margin?
    
    Geometric margin is the max width of the band that can be drawn separating the support vectors of the two classes. It is invariant to scale.
    
- SVM decision function?
    
    We use a geometric margin for any example $\vec{x}$ w.r.t $<\vec{w}, b>$, because the usual margin (given by $y_{i}(w^T \vec{x_{i}} + b)$) can be scaled without constraints. The distance of this point from the hyperplane is given by 
    
    $r = \frac{y(\vec{w}^T\vec{x}+b)}{|\vec{w}|}$
    
    Constraints:   $y_{i}(w^T \vec{x_{i}} + b)$ $>=1$ for all terms in the dataset. Geometric margin is twice $r_{min}$, which is calculated all over the dataset. So using the constraint and substituting value in the formula of $r$, we get geometric margin = $\frac{2}{|\vec{w}|}$. 
    
    We want to maximize this geometric margin (because as mentioned above, SVM needs to find a far away decision boundary). We know that $|\vec{w}| = \vec{w}^T\vec{w}$. So the final optimization problem can be written as: find $\vec{w}$ and $b$ such that:
    
    1. $\frac{1}{2}\vec{w}^T\vec{w}$ is minimized (so the reverse, which is the formula for geometric margin is maximized), and 
    2. $\forall (x_{i}, y_{i}), \quad y_{i}(\vec{w}^T\vec{x_{i}} + b) >= 1$
    
- What is a soft margin classifier?
    
    If data is not linearly separable, we should make the classifier "soft" i.e. more tolerant of mistakes by adding a cost factor (slack variable) to the optimization function. This makes a soft margin classifier. Advantage is that the feasible region is never empty: there is always a possible solution. Slack must be positive (additional constraint in SVM equation). The hyperparam C controls overfitting and underfitting. Updated equations:
    
    Find $\vec{w}$ and $b$ such that:
    
    1. $\frac{1}{2}\vec{w}^T\vec{w} + C \sum \zeta_n$ is minimized (so the reverse, which is the formula for geometric margin is maximized), and
    2. $\forall (x_{i}, y_{i}), \quad y_{i}(\vec{w}^T\vec{x_{i}} + b) \geq 1 - \zeta_n$ and $\zeta_n \geq 0$.
- What is the kernel trick?
    
    For data that is not linearly separable, we can map it to higher dimensions using a kernel function. The kernel function corresponds to a dot product in some expanded feature space. This process is called kernel trick. Types: linear kernel, polynomial kernel, Radial basis function kernel (RBF)/ Gaussian Kernel
    
- Loss function for SVM?
    
    Hinge loss solved with subgradient descent (primal approach) or dual approach using Langrangian multipliers. Can’t use normal grad desc bc hinge loss is non-differentiable at w.x+b = 1. Dual approach is better when data isnt linearly separable.
    
- Advantages and disadvantages of SVM?
    
    Effective in high dim, good classifier for linearly sep’ble data, outliers have less impact. But time consuming, hyperparams and kernel tricky, not suitable for large datasets
    
- Multi-class SVM loss?
    
    $L_i = \sum_{j \neq y_i}max(0, s_j - s_{y_i} + 1)$
    
    Basically it is computing difference between scores for incorrect labels and score for the correct label and summing them up. The logic is that the correct score should be very different from other scores.
    
- Hyperparams of svm?
    
    C - penalty factor for misclassification: high value means more penalty so smaller margin
    
    Gamma (for nonlinear kernel)