# Decision Trees

## **Decision Trees**

- What is a decision tree?
    
    A decision tree is a simple classification algorithm. We greedily build a tree during training stage and then use it for classification. If each leaf node assigns a class, then it's a decision tree, or if it assigns real values, then it's a regression tree.
    
- What is the idea behind decision trees?
    
    The most basic concept is that you're creating a tree to make decision on class labels. Each internal node in the tree is a test: we test multiple features there for some value (like entropy etc.), and select the feature with the best test value to split on. From there, the data is split further into nodes based on this node feature's values, and so on until either all features are exhausted or there are no more data samples (i.e. leaf nodes reached). 
    
- What is usually the best DT?
    
    Occams razor principle applies here. The smallest DT that fits the data is the best usually.
    
- What are some common quality measures at each node?
    
    Assume henceforth that $p(c_{i})$ means the proportion of samples with category $c_{i}$.
    
    - Entropy ( $H(X)$)
        
        $H(s) = - \sum_{i}p(c_{i})log(p(c_{i}))$
        
    - Cross entropy
        
        $H_C(X) = -\sum_i p(x_i)log q(x_i)$, where q is an approximation of p. Similar to cross entropy loss in log reg.
        
    - Relative entropy (Kullback-Leiblar convergence)
    - Joint entropy ( $H(X, Y)$)
        
        $H(x, y) = - \sum_{i}p(x, y)log(p(x,y))$
        
    - Conditional entropy ( $H(Y|X)$)
        
        $H(Y|X) = H(X, Y) - H(X)$
        
    - Mutual information ( $I(X, Y)$)
        
        $I(X, Y) = \sum_{x}\sum_{y}p(x, y)log(p(x, y))/p(x)p(y)$
        
    - Information gain ( $IG(Y|X)$)
        
        $IG(Y|X) = H(Y) - H(Y|X)$
        
    - Gain ratio (S, A)
        
        $Gain ratio(S, A) = \frac{info gain (S, A)}{Split info(S, A)}$
        
    - Split info (S, A)
        
        $Splitinfo(S, A) = -\sum_{a \in A}\frac{|S_{a}|}{|S|}log_{2}\frac{|S_{a}|}{|S|}$
        
- Info gain vs. gain ratio?
    
    Info gain prefers attributes with several values (as that leads to smaller subsets, lower entropy). If there is not much variation in the number of children each feature node has, then both IG and GR work comparably, although GR is preferable usually.
    
- How to avoid overfitting in DT?
    
    Two methods:
    
    1. Early stopping: stop when a particular threshold reached
    2. Pruning: grow full tree, then remove branches
- Pros and cons of DT?
    
    Pros:
    
    1. Less effort, data can be unnormalized and heterogenous and missing, intuitive
    
    Cons:
    
    1. Not very stable - modifying the tree data leads to full tree reconstruction.
    2. Theoretical validity questionable - algorithm is greedy, no global optimization.
    3. Efficiency
    4. Poor feature combination
- Hyperparams of DT?
    
    Split quality measure: gini impurity etc., max depth, min samples to make leaf
    
- Assumptions behind DT?
    
    Categorical labels, if continuous then they are discretized. Assumes whole training set as root, then we start calculating quality measures.