# Linear Regression

- What are the four principal assumptions of linear regression?
    1. Linearity: both dependent and independent variables should have a linear relation
    2. Errors should be independent
    3. Errors should have constant variance
    4. Errors should be normally distributed.
- What is least squares?
    
    A linear model is basically given by $y = b + \sum_{i}a_{i}x_{i}$, where b is for bias (intercept). In order to make this fit on data, we do least squares optimization: choosing weights such that $(y - x_{i}\beta_{i})^2$  is minimized. Since this is a quadratic function (expressed in matrix form as transpose product), itll always have a minima.
    
- What is multi-collinearity in regression?
    
    Multicollinearity (or collinearity) occurs when one independent variable in a regression model is linearly correlated with another independent variable. Because of this, $X^TX$ in the regression coefficients given by $(X^TX)^{-1}X^TY$ will not be invertible.
    Problems with this:
    
    1. The fitted regression coefficients (beta hat) will change substantially if one of the values of one of the x variables is changed only a bit.
    2. The variance of the estimated coefficients will be inflated, which means that it will be hard to detect statistical significance. Furthermore, it’s possible that the F statistic is significant but the individual t statistics are not.
    3. Ultimately, multicollinearity makes prediction less accurate. For a given model, the underlying assumption is that the relationships among the predicting variables, as well as their relationship with the target variable, will be the same. However, when multicollinearity is present, this is less likely to be the case.
- What is Variance Inflation Factor?
    
    To check for multicollinearity. Usually if > 10, then multicol. is high. Calculated by $\frac{1}{1 - R_j^2}$ where $R_j$ is correlation between jth feature and all the other features.
    
- Types of regression?
    1. Ordinary least squares: regular regression with square cost function
    2. Ridge: OLS + squared reg. term
    3. Lasso: OLS + linear reg. term
    4. Bayesian
- What is Bayesian regression?
    
    The aim of Bayesian Linear Regression is not to find the single “best” value of the model parameters (like in OLS. This is called frequentist approach), but rather to determine the posterior distribution for the model parameters.
    
- What are sum of squares?
    
    Total sum of squares = treatment/explained sum of squares + Residual sum of squares.
    
    $\sum(y - \bar{y})^2 = \sum(\hat{y} - \bar{y})^2 + \sum(y - \hat{y})^2$ 
    
    TSS tells us how much variation there is in the dependent var (y). ESS tells us how much variation in the dep. var the model captured, and RSS tells us how much it didn’t.
    The smaller the residual sum of squares, the better your model fits your data. A value of zero means your model is a perfect fit. One major use is in finding the coefficient of determination (R2). **The coefficient of determination is a ratio of the explained sum of squares to the total sum of squares.**
    
- pros and cons of lin reg?
    
    simple, easy to implement, when you know there is linear relation this is the best (with regularization). very sensitive to outliers, assumes linearity and feature independence.