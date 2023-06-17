# Probability & Statistics

Created: July 29, 2021 12:23 AM

[Basic Distributions](Basic%20Distributions.md)

- Difference between multivariate and multinomial?
    
    Multivariate means having more than one non-independent variable and more than two variables total. It usually connotes having many variables that have relationships with each other that don’t reduce to pure independent or pure dependent variables.
    
    Multinomial describes a single variable that can take a finite number of values, more than two.
    
    You could have a multivariate system of multinomial variables. Multivariate refers to more than two variables. Multinomial refers to more than two (but not infinity) possible values of one variable.
    
- What is a statistical model?
    
    Let the observed outcome of a statistical experiment be a sample $X_1, ...X_n$ of $n$ i.i.d. random variables in some measurable space E (usually $E \in \R$) and denote by $P$ their common distribution. A statistical model associated to that statistical experiment is a pair
    $(E, P_\theta | \theta \in \Theta)$ 
    where P is a family of probability distributions indexed by $\theta$ and measured on sample space E. $\Theta$ is any parametric set.
    
- Lagrange optimization
- Properties of Gaussian RVs:
    - Affine transformation:
        
        Consider $X \sim N(\mu, \sigma^2)$ 
        $Y = aX + b \rightarrow Y \sim N(a\mu + b, a^2 \sigma ^2)$
        
    - Sum of RVs:
        
        $X \sim N(\mu_X, \sigma^2_X)$ 
        $Y \sim N(\mu_Y, \sigma^2_Y)$ 
        $Z = X + Y \rightarrow Z \sim N(\mu_X + \mu_Y, \sigma^2_X + \sigma^2_Y)$
        
- What is unbiased estimator?
    
    Whose expected value is same as the true value.
    
- What is conditional expectation?
    
    given by $E(X|A) = \sum xP(X = x | A)$ 
    
- What is law of total expectation?
    
    Given by $E(X) = \sum_{y \in \Omega_y} E(X | Y = y)P(Y = y)$
    
- How do you compare two probability distributions?
    
    By subtracting them! It’s called Kulback-Leiblar Divergence. Given by: $D_{KL}(p||q) = \sum_ip(x_i)(log(p(x_i)) - log(q(x_i))) = \sum_ip(x_i)log(\frac{p(x_i)}{q(x_i)})$
    
- What is goodness of fit test?
    
    it tells you if your sample data represents the data you would expect to find in the actual population. Goodness of fit tests commonly used in statistics are: chi-square, Kolmogorov-Smirnov, Anderson-Darling, Shipiro-Wilk.
    

### Maximum Likelihood Estimator

- What is a maximum likelihood estimator?
    
    Given some data and a parameter β, select the parameter β the maximizes the probability of the data under that parameter. This is called max likelihood estimation. Use this only at the very beginning unless you know this won’t work.
    
    The estimator is given by $\hat{\theta}_{MLE} = arg \max_{\theta}L_{n}(\theta)$, where $L_{n}(\theta)$ is the likelihood (probability) function = $\sum_{i = 1}^nf(X_{i}; \theta)$$\sum_{i = 1}f(X_{i}; \theta)$, where all the $X_{i}$s are drawn iid from a probability density function $f$.
    
- MLE for continuous variables:
    
    Read slides here: [https://courses.cs.washington.edu/courses/cse446/20sp/schedule/lecture_2_KJ_annotated.pdf](https://courses.cs.washington.edu/courses/cse446/20sp/schedule/lecture_2_KJ_annotated.pdf)
    
- What is log likelihood?
    
    The log probability.
    
- When does the MLE fail?
- What is Markov’s inequality?
    
    For any $t > 0$ and random variable $X$, 
    
    $P(X \geq t) \leq \frac{E(X)}{t}$
    

Review this PDF: 

[](http://ciml.info/dl/v0_99/ciml-v0_99-ch09.pdf)

### Statistical Testing

- What is hypothesis testing?
    
    A form of statistical inference. We make claims, and test them using statistics. Our hypothesis is formulated in two parts: null hypothesis (H0) and alternate hypothesis (H1). We define these and then calculate a p-value using a statistical test. If the p-value is less than alpha (the significance level), then null hypothesis is rejected i.e. there is enough evidence for it to be rejected. 
    How to do it in python: [https://towardsdatascience.com/hypothesis-testing-with-python-step-by-step-hands-on-tutorial-with-practical-examples-e805975ea96e](https://towardsdatascience.com/hypothesis-testing-with-python-step-by-step-hands-on-tutorial-with-practical-examples-e805975ea96e)
    
- What is p-value?
    
    P-value is the probability of observing the data if the null hypothesis is true. A smaller p-value means a higher chance of rejecting the null hypothesis. = P(Data | H0 is true)
    
- What is multiple testing?
    
    When statistical tests are used repeatedly, for example while doing multiple comparisons
    to test null hypotheses stating that the averages of several disjoint populations are equal
    to each other (homogeneous).
    
- What is Bonferroni correction?
    
    A Bonferroni Correction refers to the process of adjusting the alpha (α) level for a family of statistical tests so that we control for the probability of committing a type I error.
    
    The formula for a Bonferroni Correction is as follows:
    
    αnew = αoriginal / n, where n: The total number of comparisons or tests being performed
    
- What is False Discovery Rate?
    
    the expected proportion of incorrectly rejected null hypotheses (type I errors) in a list of rejected hypotheses.
    
- What is statistical power?
    
    Probability of rejecting null hypothesis when it is not true. Increases with value of alpha and sample size. Default value 80%.
    
- What is confidence level?
    
    The confidence level in hypothesis testing is the probability of accepting the null hypothesis when the null hypothesis is True. Default is 95%.
    
- Easy way of remembering definitions:
    
    ![stat.jpeg](stat.jpeg)
    
- What is confidence interval?
    
    a confidence interval is an interval estimation of a parameter obtained through statistical inference. It is calculated by: [point_estimation - cv**sd, point_estimation + cv**sd] where cv is the critical value based on the sample distribution, and sd is the standard deviation of the sample.
    
- What is central limit theorem?
    
    no matter what is the population’s original distribution, when taking random samples from the population, the distribution of the means or sums from the random samples approaches a normal distribution, with mean equal to the population mean.
    
- What is law of large numbers?
    
    as the number of trials gets large enough, the average result of the trials will become closer to the expected value. For example, when you toss a fair coin 1000 times, you are more likely to see Heads half of the time than tossing a fair coin only 100 times.
    
- Difference between correlation and causation?
    
    Correlation is measure  of relationship between two variables. Causation is more difficult to capture, where x can be caused by y etc.
    
- What is Simpson’s paradox?
    
    Simpson’s paradox refers to the situations in which a trend or relationship that is observed within multiple groups disappears or reverses when the groups are combined.
    
- What is confounding variable?
    
    A confounding variable is a variable that is correlated with both the dependent variable and the independent variable. Causes Simpson’s paradox.
    

[22 Statistics Questions to Prepare for Data Science Interviews](https://towardsdatascience.com/22-statistics-questions-to-prepare-for-data-science-interviews-d5651a8b3c56)

TIP: For continuous distributions, $P(X = x) = 0.$

And if you have to calculate some pdf Y = g(X) given X = f(x), then first find cumulative distr. fn (given by P(Y<y), differentiate it to get pdf. Example below:

- PDF problem solved
    
    ![WhatsApp Image 2022-03-13 at 5.06.07 PM.jpeg](Probability%20&%20Statistics/WhatsApp_Image_2022-03-13_at_5.06.07_PM.jpeg)
    

Sampling main concept:

If $X_1, X_2, ... X_n$ are samples drawn from a population with mean $\mu$ and variance $\sigma^2$, then their mean $\bar{X} = \sum X_i / n$ follows a normal distribution with mean $\mu$ and variance $\sigma^2/n$.