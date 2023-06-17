# Logistic Regression

Input X shape: n_samples, n_features

weights shape: n_features, 1

bias shape: 0

y shape: n_samples, 1

y_pred = X.w + b, shape = n_samples, 1

dw = 1/n*X^T.(y_pred - y), shape = n_features,1

db shape = n_features, 1

Basic equation: $y_{pred} = \sigma(W^TX + b)$

where the shapes of everything are above according to numpy

Gradient descent:

$C(w) = y*log(h(x)) + (1 - y)*log(1 - h(x))$

where $h(x) = y_{pred}$

Derivatives:

$dw = x.(y_{pred} - y)/n\_samples$

$db = (y_{pred} - y)/n\_samples$

Gradient update:

$w = w - \alpha*dw$, similarly for bias

- What is the effect of scaling in log reg?
    
    Ideally no effect, but regularization can make the parameters dependent on scale.
    
- Why is log reg called that despite it being a classification algo?
    
    Because it is emphatically NOT a classification algo. It is mainly used for regression, but if you provide a threshold then it is converted to a classifier.
    

Important derivations:

![WhatsApp Image 2022-03-02 at 12.02.50 PM.jpeg](Logistic%20Regression%20dda8168695204daca2771a67fe01198d/WhatsApp_Image_2022-03-02_at_12.02.50_PM.jpeg)

- pros and cons of log reg?
    
    Efficient on linearly sepble data, very easy to implement and train, can be extended to multi class. But overfits, can work with linearly sepble data mostly, assumes no multicollinearity present