# Clustering algorithms

## KNN

- What is this algorithm about?
    
    Aims to partition data into clusters in which each obs. belongs to the cluster with the nearest mean.
    
- Comments on performance (read)
    
    Fast algorithm, so can run multiple times with different start points. Does not converge to global optimum, instead local. Is computationally NP hard.
    

## DBSCAN

- What is this algorithm about?
    
    Stands for density based spatial clustering of applications with noise. Better than kmeans. Used to separate clusters of high density from clusters of low density. It can account for multi-dimensional data and create clusters of various shapes which is smth kmeans cannot do. Advs: robust towards outliers, handles high dimensional data but can struggle with clusters of similar density.
    

## Gaussian Mixture Models (Using Expectation Maximization)

- What is EM?
    
    Algorithm for Max Likelihood Estimation in the presence of latent variables (eg. training data without labels. labels are latent here)
    
- What is mixture model?
    
    A mixture model is a model comprised of an unspecified combination of multiple probability distribution functions. The Gaussian Mixture Model, or GMM for short, is a mixture model that uses a combination of Gaussian (Normal) probability distributions and requires the estimation of the mean and standard deviation parameters for each. EM algo is used for estimating parameters of GMM. Basically GMM is used for soft clustering with probabilities compared to Kmeans which is hard clustering. It assumes its clusters are Gaussian with individual means and variances, and we estimate these using EM.
    
- Two steps in EM algorithm
    
    Expectation maximization for mixture models consists of two steps.
    
    The first step, known as the expectation step or E step, consists of calculating the expectation of the component assignments $C_k$ for each data point $x_i \in X$ given the model parameters $\phi_k$, $\mu_k$, and $\sigma_k$.
    
    The second step is known as the maximization step or M step, which consists of maximizing the expectations calculated in the E step with respect to the model parameters. This step consists of updating the model parameters $\phi_k$, $\mu_k$, and $\sigma_k$.
    

Read more here

[Gaussian Mixture Model | Brilliant Math & Science Wiki](https://brilliant.org/wiki/gaussian-mixture-model/)

Which model to use when?

DBSCAN when you don’t know k. GMM for soft clustering, kmeans/kmodes for hard.