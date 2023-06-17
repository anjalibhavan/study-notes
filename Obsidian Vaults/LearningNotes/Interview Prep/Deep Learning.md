# Deep Learning

Created: November 18, 2021 5:29 PM

## Deep Learning

- Why do we want zero-mean data?
    
    So we have positive and negative values, and gradients are not all of the same sign. very inefficient gradient updates otherwise.
    

### 1. Back-propagation

- Backprop equations?
    
    $\frac{\partial C}{\partial w^{l}} = \frac{\partial C}{\partial a^{l}}\frac{\partial a^{l}}{\partial z^{l}}\frac{\partial z^{l}}{\partial w^{l}} \\ \\ \\ \frac{\partial C}{\partial b^{l}} = \frac{\partial C}{\partial a^{l}}\frac{\partial a^{l}}{\partial z^{l}}\frac{\partial z^{l}}{\partial b^{l}}$
    
- Why is backprop needed?
    
    Backpropagation is the learning mechanism that allows the Multilayer Perceptron to iteratively adjust the weights in the network, with the goal of minimizing the cost function.
    

### 2. Optimizers

- What are exponentially weighted averages?
    
    A component of several optimization algorithms. Better than gradient descent. Equation is given by $V_{t} = \beta V_{t-1} + (1 - \beta)\theta _{t}$
    
- What do optimizers in a neural network achieve?
    
    The non-linearity of neural networks causes most loss functions to become nonconvex. This means NNs are usually trained by iterative gradient-based optimizers.
    
- What is the issue with too high or too low LR in gradient descent?
    
    A learning rate that is too small leads to painfully slow convergence, while a learning rate that is too large can hinder convergence and cause the loss function to fluctuate around the minimum or even to diverge.
    
- A problem with SGD?
    
    Saddle points: when one side of the point is increasing, one side decreasing. These saddle points are usually surrounded by a plateau of the same error, which makes it notoriously hard for SGD to escape, as the gradient is close to zero in all dimensions. Also get stuck in local minima. But in higher dimensions saddle points > local minima bc we see more frequently losses going up and down (saddle), not up at the same time as our network and dimensions grow.
    
- What is momentum?
    
    SGD starts oscillating a lot when it reaches saddle points/ravines. To correct that we introduce a momentum term. Momentum dampens oscillations. The momentum term increases for dimensions whose gradients point in the same directions and reduces updates for dimensions whose gradients change directions. As a result, we gain faster convergence and reduced oscillation. Here v stands for velocity. We usually initialize it to 0 (i.e. v_0 = 0).
    $v_t=γv_{t-1}+η∇_{θ}J(θ) \\ θ_t=θ_{t - 1}−\alpha v_{t}$
    
- What is NAG?
    
    An improvement over momentum: gives momentum a direction. We know that we will use our momentum term γvt−1 to move the parameters θ. Computing θ−γvt−1 thus gives us an approximation of the next position of the parameters. So the equations become:
    
    $v_t = \gamma v_{t-1} + \eta \nabla_\theta J(\theta - \gamma v_{t - 1})$
    
    $\theta = \theta - v_t$
    
- What are RMSProp and Adagrad?
    
    Another way of improving SGD. Instead of velocity like in momentum, we compute accumulated squared gradient, then divide update by square root of this accumulation. RMSProp lets the accumulated sq grad decay a bit over time by adding a decay term.
    
- Why does Adagrad work well for sparse data?
    
    It adapts the learning rate to the parameters, performing smaller updates
    (i.e. low learning rates) for parameters associated with frequently occurring features, and larger updates (i.e. high learning rates) for parameters associated with infrequent features. For this reason, it is well-suited for dealing with sparse data.
    
- Limitations of Adagrad?
    
    its accumulation of the squared gradients in the denominator: Since every added term is positive, the accumulated sum keeps growing during training. This in turn causes the learning rate to shrink and eventually become infinitesimally small, at which point the algorithm is no longer able to acquire additional knowledge.
    
- What is Adam?
    
    Combines both velocity stuff from momentum and squared gradients stuff from Adagrad.
    
- Note on L-BFGS
    
    All the optimizers we have seen till now are first-order optimizers i.e. they compute first order derivatives and use a linear approximant and learning rate (LR). We can instead compute second order derivatives, a Hessian matrix and do away with LR, and approximate our fn with quadratic curve. This is great but impractical bc Hessian is n*n where n is number of parameters in network. So algos like L-BFGS try to make a low-rank approximn. Not very good algo tho.
    

### 3. Other topics

- What are vanishing/exploding gradients? How do we check for them?
    
    When weights increase/decrease exponentially with i/p layer. Partial solution: careful initialization of weights. More detail for the case of sigmoid activation (z is output after applying sigmoid:
    
    If your weight matrix W is initialized too large, the output of the matrix multiply could have a very large range (e.g. numbers between -400 and 400), which will make all outputs in the vector z almost binary: either 1 or 0. But if that is the case, z*(1-z), which is local gradient of the sigmoid non-linearity, will in both cases become zero (“vanish”), making the gradient for both x and W be zero. The rest of the backward pass will come out all zero from this point on due to multiplication in the chain rule.
    
    If the largest singular value of the weight matrix is > 1, then exploding gradient. < 1 then vanishing. For exploding we can do gradient clipping: divide gradient by some threshold.
    
- What is Xavier initialization?
    
    Used for careful initialization of weights to solve vanishing/exploding gradients. 
    If Relu activation, multiply by $\sqrt{2/n^{l-1}}$, if tanh, same but 1 instead of 2.
    
- Why is it "feed forward" neural network? why are there no loops in a NN?
    
    Because we could then get a situation where the input depended on the output, which is tough to make sense of.
    
- Why do we initialize neural network weights with random values rather than 0 (as done in log reg: why that? read online)
    
    Because if we initialize weights with 0, then all neurons in first hidden layer will perform the same computation. Then all the subsequent neurons also, so no learning going on.
    
- What is the difference between hyperparameters and parameters?
    
    Hyperparams are external to the model: we manually set them, they help w model training etc. Params are internal and figured out by the estimator in hand.
    
- Should you overfit or underfit a neural network first?
    
    Overfit on a few examples to ensure the lowest possible loss is being achieved.
    
- Why do we shuffle dataset?
    
    So model does not learn from any underlying patterns in sequence of data samples.
    

### 4. Activation functions

- Why activation at all?
    
    The more complicated the information, the more non-linear the mapping of features to the bottom truth label will usually be. If there is no activation function in a neural network, the network would in turn not be able to understand such complicated mappings mathematically and wouldn’t be able to solve tasks that the network is really meant to resolve. It will function like a linear regression system.
    
- Advantages and disadv. of sigmoid
    1. Because its change in output is a linear function of change in weights and biases. So makes it easier to figure out impact.
    2. When extreme values pass through sigmoid, the values saturate and the gradient is killed off to nearly 0. thus difficult for network to learn weights meaningfully.
    3. When input is always positive or negative, all of the gradients will also be always +ve or -ve. It leads to very inefficient gradient updates.
    4. Exp() is compute expensive (minor point)
- Advantages and disadv. of relu
    
    Relu helps with SGD and is scale invariant. Does not saturate in +ve space. Comput. efficient.
    Dead Neurons: If the units are not activated initially, then they are always in the off-state as zero gradients flow through them (Dead Neurons). This can be solved by enforcing a small negative gradient flow through the network (Leaky ReLU). The negative coefficient can also be learned as a parameter like in PReLU. we might expect learning to be slow when training ReL networks with constant 0 gradients. Called dying Relu problem.
    
- Advantages and disadv. of tanh
    
    Squashes inputs to -1, 1 which is better than sigmoid. But also kills gradients like sigmoid.
    
- Advantages and disadv. of maxout
    
    Maxout is given by $max(w_1x+b, w_2x+b)$. Does not saturate, does not kill gradients, but doubles parameters per neuron: instead of w, we have w1 and w2.
    
- All activation functions graphs and formulas?
    1. ReLU: 
    $f(x) = x, x \geq 0; 0, x < 0$
    2. Tanh:
    $f(x) = \frac{1 - e^{-2x}}{1 + e^{-2x}}$
    3. Sigmoid:
    $f(x) = \frac{1}{1 + e^{-x}}$
    4. Parametric ReLU:
    $f(x) = x, x \geq 0; ax, x < 0$
- Read link
    
    [Activation Functions | What are Activation Functions](https://www.analyticsvidhya.com/blog/2021/04/activation-functions-and-their-derivatives-a-quick-complete-guide/)
    
- What if we preprocess and make data zero mean? can we still use sigmoid?
    
    Solves the problem for first layer but doesnt work for deeper networks.
    

### 5. Batch Normalization

- What is batch normalization?
    
    Normalizing layer outputs for easier training of weights and biases. Either z or a, z more common. z is the output before activation.
    
    $z^{l} = \gamma ^{l}z_{norm}^{l} + \beta ^{l}$, where gamma is $\sqrt{\sigma ^{2} + \epsilon}$ and beta is mu. Gamma and mu are computed over each minibatch.
    
- Advantages?
    
    Batch norm reduces the width of the distribution of the zs, so it makes the job of later layers easier. Reduces strong dependence on initialization. Allows higher learning rates. Batch normalization standardizes the distribution of layer inputs to combat the internal covariance shift. It controls the amount by which the hidden units shift. Consider this example to understand the covariance shift. If we train a network to detect brown dog images and later you end applying this network to data with colored dog images it would not be able to perform well and we would have to train again. This change in the distribution of input is the covariance shift.
    
- Miscellaneous point (read)
    
    When working with minibatches, take mu and sigma of just that minibatch. However at test time we process one example at a time. To solve this, we estimate mu and sigma for test time using exponentially weighted averages (across minibatches).
    

## Transformers

Resources to read:

[](https://www.dropbox.com/s/rahrg6s7w4vud9f/lecture12_attention_neural_networks.pdf?dl=0)

[](https://www.shane.st/teaching/575/spr21/slides/2_LMs.pdf)

- What is a transformer?
    
    Consists of encoder layer followed by decoder. Massive pretraining and then finetuning on other tasks and data.
    
- What is in a transformer block?
    
    Multihead attention → add and norm → feed forward → add and norm
    
- What is self-attention?
    
    If a sentence is like “the dog didn’t cross the street because it was too tired”, self-attention allows the network to reference “the dog” for “it” instead of “the street”. Basically it allows the network to consider other positions in the input sequence.
    
    How to calculate self-attention:
    
    1. For each word, calculate query, value and key vector.  (use a matrix consisting of all word embeddings for faster processing.) These are calculated by multiplying word embeddings with Query, Key and Value matrices we train during training process.
    2. Then the output is given by:
    $Z = softmax(\frac{Q \times K}{\sqrt[2][d_k]})*V$
    
    $d_k$ is the square root of query vector embedding dimensions i.e. 8 by default.
    
- What is multi-headed attention?
    
    Same self-attention calculation but done multiple times. Multiply the initial embedding matrix with 8 different weight matrices to get 8 trios of q,k,v matrices (each is called an attention head). Then get 8 outputs, concatenate them and multiply with another weight matrix you train simultaneously during the training process. The result is the output Z which is sent ahead to other layers.
    
- Advantage of multi-head attention over self?
    1. It expands the model’s ability to focus on different positions. Yes, in the example above, z1 contains a little bit of every other encoding, but it could be dominated by the the actual word itself. 
    2. It gives the attention layer multiple “representation subspaces”.
- What is positional encoding?
    
    A vector added to the initial embedding matrix to codify the order of words in the input sequence.
    
- What is ELMO?
    
    Gives contextualized word embeddings. Instead of using a fixed embedding for each word, ELMo looks at the entire sentence before assigning each word in it an embedding. It uses a bi-directional LSTM trained on a specific task to be able to create those embeddings. 
    
- What does BERT consist of?
    
    Masked Language Modelling and Next Sentence Prediction
    
- What happens in test time in RNN?
    
    We input a prefix to the input layer. This gives an output in the first time step as softmax probabilities. Instead of taking argmax and proceeding, we can instead sample from this distribution; leads to model diversity. The sampled output is now fed as input to next time step, and so on till the end.
    
- LSTM equations?
    
    ![WhatsApp Image 2022-03-13 at 5.06.07 PM.jpeg](Deep%20Learning/WhatsApp_Image_2022-03-13_at_5.06.07_PM.jpeg)
    
- What is a seq2seq model?
    
    Consists of encoder and decoder, both are LSTMs.
    
    - The initial states of the decoder are set to the final states of the encoder.
    - The initial input to the decoder is always the START token.
    - At each time step, we preserve the states of the decoder and set them as initial states for the next time step.
    - At each time step, the predicted output is fed as input in the next time step.
    - We break the loop when the decoder predicts the END token.

[https://www.analyticsvidhya.com/blog/2020/08/a-simple-introduction-to-sequence-to-sequence-models/](https://www.analyticsvidhya.com/blog/2020/08/a-simple-introduction-to-sequence-to-sequence-models/)