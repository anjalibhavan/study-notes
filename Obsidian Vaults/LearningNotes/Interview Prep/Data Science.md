# Data Science

Created: February 23, 2022 10:17 AM

- Why should we normalize train and test set?
    
    Coz weights come into a smaller range therefore need less learning rate to converge. Data scaling is especially important in large neural networks, since it helps speed up gradient descent
    
- Ask shivin and kunal: Bagging generally improves unstable methods, such as neural networks, classification and regression trees, and subset selection in linear regression. However, it can mildly degrade the performance of stable methods such as k-nearest neighbors. which ones are stable/unstable and why?
- Handling imbalanced data?
    
    Three ways: subsampling (remove some majority label data points) or weighing (assign unequal weights to majority and minority samples), oversampling(add copies of minority label data points)
    
    Another way is data augmentation: instead of oversampling by adding copies, add copies with slight perturbations. SMOTE (Synthetic Minority Oversampling Technique) is used for this.
    
- What is SMOTE algorithm?
    1. You draw a random sample from the minority class.
    2. For the observations in this sample, you will identify the k nearest neighbors.
    3. You will then take one of those neighbors and identify the vector between the current data point and the selected neighbor.
    4. You multiply the vector by a random number between 0 and 1.
    5. To obtain the synthetic data point, you add this to the current data point.
- Impact of using SMOTE?
    
    The result of using SMOTE is generally an increase in recall, at the cost of lower precision.
    
- How do we handle missing data?
    
    We check for missing values using isnull() in Pandas. To fill them in we use fillna(), replace() or interpolate(). To remove those rows we use dropna().
    
    1. Imputation: replacing missing values with mean/median of non-missing ones.
    2. Imputation: replacing missing values with zero/constant/most frequent values
    3. Imputation using KNN
    4. Imputation using MICE - Multivariate Imputation by Chained Equation (basically filling missing data multiple times)
    5. Imputation using deep learning
- How to clean data?
    
    Remove HTML, tokenization + remove punctuation, remove stopwords, lemmatization/stemming
    
    [https://towardsdatascience.com/nlp-for-beginners-cleaning-preprocessing-text-data-ae8e306bef0f](https://towardsdatascience.com/nlp-for-beginners-cleaning-preprocessing-text-data-ae8e306bef0f)
    
    - Rescaling attributes with different scales
    - Standardizing the dataset
    - Encoding categorial attributes with integer values
    - Handling missing data
    - Removing duplicated data points
    - Removing outliers/ handle noisy data
    - Discretize the data
    - Split the dataset into a training and test set
- Types of data sampling?
    1. Regular random sampling
    2. Stratified sampling: ensures equal proportions of classes present
    3. Cluster stratified sampling: divides population into clusters. What makes this different that stratified sampling is that each cluster must be representative of the population. Then, you randomly selecting entire clusters to sample. Fast and efficient, but not always possible
    4. Systematic random sampling: is a very common technique in which you sample every k’th element. Fast but not v feasible.
- What cross-validation technique should you use on a time series data set?
    
    The default cross-validation techniques shuffle the data before splitting them into different folds, which is undesired for time series analysis. There are two methods: “sliding window” and “forward chaining”. First, we preserve the order of our data and slicing them into different folds. In the sliding window, we train on fold 1 and test on fold 2. Then we train on fold 2 and test on fold 3. We will finish until we test the last fold. In the forward chaining, we train on fold 1, test on fold 2. Then we train on fold 1+2, test on fold 3. Then train on fold 1+2+3, test on fold 4. We will stop until we test the last fold.