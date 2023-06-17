# K Nearest Neighbors

- What is the KNN classifier based on?
    
    This classifier is based on simple majority voting. It is an example of lazy learning: there is no actual training going on. The model just stores all the training instances, then during test time the closest $k$ neighbors of the given test sample are selected, and label selected based on majority/weighted voting.
    
- How to choose param k?
    
    The best choice of *k* depends upon the data; generally, larger values of *k* reduces effect of the noise on the classification, but make boundaries between classes less distinct. A good *k* can be selected by various [heuristic](https://en.wikipedia.org/wiki/Heuristic_(computer_science)) techniques (see [hyperparameter optimization](https://en.wikipedia.org/wiki/Hyperparameter_optimization)). There are no pre-defined statistical methods to find the most favorable value of K. Larger K means overfitting (high variance low bias), smaller K means vice versa.
    
- Pros and cons of KNN?
    
    No assumptions bc non-parametric model. Intuitive, simple, works really well. One hyperparameter, no training. But: slow, curse of dimens., sensitive to outliers and imbalanced data, choosing k difficult bc no statistical method.