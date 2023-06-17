# Naive Bayes

- What is the idea behind Naive Bayes?
    
    It's a probabilistic model. So for each input $X$, you want to find the class with the highest probability. That class is the label for $X$. We use the Bayes' rule for this:
    
     $P(B|A) = P(A|B)*P(B)/P(A)$
    
- Naive Bayes equations?
    
    Say $X = (f_{1}, f_{2}...f_{k})$. We want to find $c^{*} = argmax(P(c|x))$.
    
    Applying Bayes' rule: 
    
    $c^{*} = argmax(P(X|c)P(c)/P(X)) = argmax(P(X|c)P(c))$ ( since $P(X)$ is a constant). 
    
    Now, $P(X|c) = P(f_{1}...f_{k}|c) = \prod_{j}P(f_{j}|c, f_{1}...f_{j-1})$
    
    Here comes the naive assumption: that all features are conditionally independent. 
    
    So $P(X|c) = \prod_{j}P(f_{j}|c)$
    
- How many model parameters does NB have?
    
    NB has two types of model params: class priors ($P(c)$, which are $|c|$ in number) and conditional probabilities ($P(f_{j}|c)$, which are $|f|*|c|$ in number).
    
- What is Zipf's law?
    
    Zipf's law, also called the long tail phenomenon, states that only a small number of events occur with high frequency, and a large number occur with low frequencies.
    
- What is the multivariate NB model?
    
    In a multivariate NB model, all features are binary. And all features, including the absent ones, are used in classification. According to this model, each document is a result of $|V|$ independent Bernoulli experiments i.e. for each word, does it appear in the doc?
    
    Classify $d_{i} = argmax_{c}P(c)P(d_{i}|c) = \prod_{w_{k} \in d_{i}}P(w_{k}|c)\prod_{w_{k} \notin d_{i}}(1 - P(w_{k}|c))$
    
- What is the multinomial NB model?
    
    In multinomial model, every word *position* is a trial - unlike in multivariate in which every document was the result of $|V|$ trials. Here we are also considering word counts, there we were factoring in only absence and presence. The probability of a word $w_{t}$ having class label $c_{j}$ is given by the number of times it appears in that doc times the probability of its occurrence, divided by the same product taken over all words of the vocabulary.
    
    Testing stage: $classify(d_{i}) = argmax_{c}P(c) \prod_{k = 1}^{|V|}P(w_{k}|c)^{N_{ik}}$
    
- Strengths of NB?
    
    Simplicity, efficiency, scalability
    
- Weaknesses of NB?
    
    Theoretical validity, prediction accuracy
    
- Assumptions of NB?
    
    Features are condiitonally independent given class