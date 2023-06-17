
1. Bernoulli: Discrete distribution. Assumptions: Two outcomes, success or fail. One trial. Expectation = p, variance = p(1 - p)
2. Binomial: Discrete distribution. x is the number of successes in n Bernoulli trials. PMF given by 
$nC_xp^x(1-p)^{(n-x)}$. Expectation = np, variance = np(1-p).
3. Poisson: Discrete distribution. For modeling events in a fixed time interval.
4. Uniform: models a random variable whose outcomes are equally likely to happen. The outcomes can be discrete, like the outcomes getting form tossing a die, or continuous, like the waiting time for a bus to arrive. Thus Uniform distribution can be a discrete or continuous distribution depending on the random variable. PMF is $f(x) = 1/(b - a), x \in [a, b]$ Expectation is a + b / 2 and variance (a - b)^2/12
5. Normal: Continuous distribution. Mean=median=mode = mu. 
6. Exponential: Continuous distribution. Models time intervals in between Poisson events. Memoryless distribution.
7. Geometric: Models number of failures before first success in n Bernoulli trials. PMF is $(1-p)^xp$
expectation = (1-p)/p, variance = (1-p)/p^2. Memoryless distribution.

[Seven Must-Know Statistical Distributions and Their Simulations for Data Science](https://towardsdatascience.com/seven-must-know-statistical-distributions-and-their-simulations-for-data-science-681c5ac41e32)