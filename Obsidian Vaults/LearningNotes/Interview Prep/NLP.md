# NLP

Created: July 29, 2021 1:08 AM

## Definitions

- What is TFIDF?
    
    Stands for term frequency-inverse document frequency. Is used to see how important a term is in the corpus. Formula:
    TF: count of word in doc/total words in document
    
    IDF: ln(total number of documents in corpus/number of documents this word appears in)
    
- What is the difference between stemming and lemmatization?
    
    Stemming doesn't give word roots that are actual form, always. Eg - 
    stemming: writing → writ + ing
    lemmatization: writing → write + V + prog
    
- What is density estimation?
    
    The goal of density estimation is to estimate the unknown probability density function of a random variable from a set of observations. In more familiar language, density estimation smoothes collections of individual measurements into a continuous distribution, replacing points on a line or plane by a smooth estimator curve or surface.
    
- Why are LMs called density estimators?
    
    Language modeling tries to capture the notion that some sentences are more likely than others by density estimation P (s). In particular, we want the model to satisfy P (s1) > P (s2)
    
- What is smoothing?
    
    Some words in a vocab appear in unseen contexts. To keep from assigning zero prob, we do smoothing. Ways: Laplace (add-one) smoothing, add-k smoothing, stupid backoff, and Kneser-Ney smoothing.
    
    Add-one and add-k basically add 1 or k to numerator and denominator so there are no zero probs. An alternative is **discounting** which lowers some non zero probs. 
    Backoff uses an ngram hierarchy:  we use the trigram if prob is nonzero, otherwise we use the bigram, otherwise the unigram. In interpolation we consider all three ngrams and sum their probs up with weights lambda_i.
    

## Models

- What is CRF?

Some NLP code links:

[Interview-prep/Interview Prep.ipynb at master · raydeng2007/Interview-prep](https://github.com/raydeng2007/Interview-prep/blob/master/Interview%20Prep.ipynb)

- Why is it not good to have higher values for n in ngram?
    
    small training data means there will be many n-grams that do not appear
    in the training text. This problem is exacerbated when a more complex
    model is used: a 5-gram in the training text is much less likely to be
    repeated in a different text than a bigram does.
    
- When to use ngrams? Why neural over ngrams?
    
    ngrams cannot capture long-distance dependencies. And need the test data to be from same distribution as train data. So do not generalize very well.
    
- Problems with softmax layer?
    
    the cost of computing the softmax is proportional to the number of words in V, which is typically on the order of hundreds of thousands or millions.
    
- What two architectures for learning word embeddings did Mikolov propose in Word2Vec paper?
    1. CBOW: Continuous bag of words. We use both the n words before and after the target word wt to predict it. Called CBOW because continuous repr. with no emphasis on word order. Objective function:
        
        $J_θ=1/T \sum^T_{t=1} ∑_{−n≤j≤n,≠0}log p(w_{t}|w_{t - n}...w_{t - 1}, w_{t + 1}, ... w_{t + n})$
        
    2. Skip-gram: turns LM concept on its head, and instead uses one word to predict the n surrounding words. The objective function becomes 
    $J_θ=1/T \sum^T_{t=1} ∑_{−n≤j≤n,≠0}log p(w_{t+j}|w_t)$
- What’s the difference between count-based and prediction-based word embeddings?
    
    GloVe is count-based and Word2Vec is prediction-based. Count-based models learn their vectors by essentially doing dimensionality reduction on the co-occurrence counts matrix. Predictive models learn their vectors in order to improve their predictive ability of Loss(target word | context words; Vectors), i.e. the loss of predicting the target words from the context words given the vector representations. In word2vec, this is cast as a feed-forward neural network and optimized as such using SGD, etc.
    
- What goes in a tokenizer?
    
    Two things: token segmenter and token learner. Learner takes corpus and induces a set of tokens. Segmenter segments the sentences into tokens. Three types of segmenters: byte-pair encoding, unigram language modeling and WordPiece (used in BERT)
    
- Why is sparsity particularly bad in NLP?
    
    There are two kinds of sparsity: data sparsity and model sparsity. Model sparsity can be good because it means that there is a concise explanation for the effect that we are modeling. Data sparsity is usually bad because it means that we are missing information that might be important. Data sparsity is more of an issue in NLP than in other machine learning fields because we typically deal with large vocabularies where it is impossible to have enough data to actually observe examples of all the things that people can say. There will be many real phrases that we will just never see in the training data.
    
- How to handle sparsity?
    
    Using the SVD to compress the matrix gives us dense low-dimensional vectors for each word. This is a way of sharing information between similar words to help deal with the data sparsity. Another thing that people sometimes do to deal with sparsity is to use sub-word units instead of words or to use stemming or lexicalization to reduce the vocabulary size.
    
- What is LDA?
    
    LDA is a probabilistic topic model and it decomposes documents into topics in a similar way as a Gaussian mixture model (GMM) decomposes continuous data into Gaussian densities. Differently from the GMM, an LDA models discrete data (words in documents) and it constrains that the topics are a priori distributed according to a Dirichlet distribution.
    
- What is BLEU score?
    
    (Bilingual Evaluation Understudy)
    It is mostly used to measure the quality of machine translation with respect to the human translation. It uses a modified form of precision metric.
    

## Ambiguity

- Two types of lexical disambiguation?
    
    Part-of-speech (whether duck is a verb or noun), word sense disambiguation (whether make means create or cook).
    

## Speech Processing

- Most important features of acoustic signal?
    1. Resonance of vocal tract (esp. formants F1 and F2 which are two lowest)
    2. Fundamental frequency of speech signal
    3. Signal amplitude
- Hierarchy of speech?
    
    At the lowest level of hierarchy, there are phones, which are considered as physical realizations of more abstract phonemes. Sequences of phones are organized into syllables, and syllables make up words (where each word consists of one or more syllables)
    
- What are phones?
    
    the elementary units of speech, associated with articulatory gestures responsible for producing them and with acoustic cues that make them distinct from other phones. Phonetic transcription is the process of marking down phones of speech with symbols (denoted with brackets [ ]). Phonetic transcription often makes use of the International Phonetic Alphabet (IPA). On a high level, phones can be divided into vowels and consonants. While all vowels are voiced sounds, consonants can be voiced or unvoiced.
    
- What is prosody?
    
    [Prosody](https://en.wikipedia.org/wiki/Prosody_(linguistics)) aka. suprasegmental phenomena in speech refers to those patterns in speech that take place at time-scales larger than individual phones (segments)
    
- What is pitch?
    
    Pitch refers to our perception of the frequency of a tonal sound.
    
- What is Fourier transform? Why is it a good thing?
    
    Fourier transform (FT) is a mathematical transform that decomposes functions depending on space or time into functions depending on spatial or temporal frequency. Linear operations performed in one domain (time or frequency) have corresponding operations in the other domain, which are sometimes easier to perform. The operation of differentiation in the time domain corresponds to multiplication by the frequency, so some differential equations are easier to analyze in the frequency domain. Also, convolution in the time domain corresponds to ordinary multiplication in the frequency domain.
    
- What is discrete fourier transform?
    
    It maps a length N signal xn into a complex valued frequency domain representation Xk of N coefficients as:
    
    $X_k = \sum_{n = 0}^{N - 1}x_ne^{-i\frac{2\pi kn}{N}}$
    
- What is the log spectrum?
    
    The log-spectrum 20log10|Xk| is the most common visualization of spectra and it gives the spectrum in decibels. It is useful because again, it gives a visualization where sounds can be easily interpreted.
    
- Advantages of log spectrum?
    
    The logarithmic spectrum, on the other hand, is a much more accessible representation. It is not only more visual, but importantly, the logarithm approximates roughly the sensitivity of the ear, such that logarithmic spectra can be used to assess auditory importance of spectral features. The logarithmic spectrum visualizes spectral content such that the magnitude of values is approximately uniform throughout the spectrum.
    
- What is cepstrum?
    
    Taking fourier transform of the log spectrum:
    $∣F^{−1}\{{log(|F\{{x(t)}\}|^2)}∣\}∣^2$
    
- What is Mel scale?
    
    $m = 2595log_{10}(1+f/700)$