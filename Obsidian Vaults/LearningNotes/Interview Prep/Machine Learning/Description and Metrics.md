# Description and Metrics

- Types of models?
    1. Point-wise models: which try to predict a (matching) score for each query-document pair in the dataset, and use it for ranking the items.
    2. Pair-wise models: which try to learn a binary classifier that can tell which document is more relevant to a query, given pair of documents.
    3. List-wise models: which try to directly optimize the value of one of the above evaluation measures, averaged over all queries in the training data.

### Metrics for ranking algos

- DCG/NDCG
    
    NDCG: Normalized Discounted Cumulative Gain, $DCG = \sum_k \frac{2^{rel_i} - 1}{log_2(i + 1)}$  where reli = 1 if document is relevant else 0. Comes from Cumulative Gain: $= \sum_k rel_i$. DCG can also be written as $DCG = \sum_k \frac{rel_i - 1}{log_2(i + 1)}$ . NDCG is normalized DCG: divide DCG by idealized DCG.
    
    $NDCG = \frac{DCG}{IDCG}$, $IDCG = \sum_i^{|rel_k|} \frac{2^{rel_i} - 1}{log_2(i + 1)}$ 
    
- Mean reciprocal rank (MRR)
    
    MRR is essentially the average of the reciprocal ranks of “the first relevant item” for a set of queries Q.
    
- Precision at k/ Recall at k
    
    the number of relevant documents among the top k documents. 
    
- Mean Average Precision

[](https://towardsdatascience.com/20-popular-machine-learning-metrics-part-2-ranking-statistical-metrics-22c3e5a937b6)

Limitations of ranking metrics:

1. One of the limitations of MRR is that, it only takes the rank of one of the items (the most relevant one) into account, and ignores other items (for example mediums as the plural form of medium is ignored). This may not be a good metric for cases that we want to browse a list of related items.
2. P@k has several limitations. Most importantly, it fails to take into account the positions of the relevant documents among the top k. Also it is easy to evaluate the model manually in this case, since only the top k results need to be examined to determine if they are relevant or not.
3. In contrast to the previous metrics, NDCG takes the order and relative importance of the documents into account, and values putting highly relevant documents high up the recommended lists.
4. MAP can be adapted to multilabel problems, at the cost of an approximation
MAP does not need to be computed at k but the multilabel version might not be adapted when the negative class is preponderant
5. NDCG is a popular metric, but has its own limitations too. One of its main limitations is that it does not penalize for bad documents in the result. It may not be suitable to measure performance of queries that may often have several equally good results (especially true when we are mainly interested in the first few results as it is done in practice).