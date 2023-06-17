# HMM

- What is HMM?
    
    Statistical model used for modeling sequences of observations over time. It has state (hidden) sequences and output sequences. Given output sequences, we need to recover the hidden sequence. 
    
- Two Markovian assumptions behind HMM?
    1. Limited horizon assumption: probability of state at time t depends only on state at time t - 1
    2. Stationery assumption: conditional dist over next state given current state does not change over time
- Two types of probabilities?
    1. Transition probs: from one state to another
    2. Emission probs: from state to output symbol
- Probability of a state sequence equation
    
    $P(\vec{z}) = P(z_t,...z_1; A)$ where $A$ is the transition probability matrix
    
    $= \prod_{t = 1}^TA_{z_{t-1}z_t}$
    
- Maximum likelihood estimate
    
    $l(A) = logP(\vec{z};A)$
    
    $= log \prod_{t = 1}^TA_{z_{t - 1}z_t} = \sum_{t = 1}^T logA_{z_{t - 1}z_t}$