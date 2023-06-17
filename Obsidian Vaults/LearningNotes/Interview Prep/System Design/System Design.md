# System Design

Created: July 30, 2021 10:54 PM

Sourced from: 
Steps in ML system design and questions to ask interviewer:

[Machine learning systems design](https://huyenchip.com/machine-learning-systems-design/toc.html)

[https://medium.com/double-pointer/system-design-interview-autocomplete-type-ahead-system-for-a-search-box-1ac968f9f121](https://medium.com/double-pointer/system-design-interview-autocomplete-type-ahead-system-for-a-search-box-1ac968f9f121)

[https://leetcode.com/discuss/interview-question/system-design/566057/Machine-Learning-System-Design-%3A-A-framework-for-the-interview-day](https://leetcode.com/discuss/interview-question/system-design/566057/Machine-Learning-System-Design-%3A-A-framework-for-the-interview-day)

[ML Systems Design Interview Guide · Patrick Halina](http://patrickhalina.com/posts/ml-systems-design-interview-guide/)

^^ use this for links to recommender systems problems.

Spam filtering, pinterest home feed

[Recommender system points](Recommender%20system%20points.md)

[Booking.com](http://booking.com/) go to some lengths to minimise the latency introduced by models, including horizontally scaled distributed copies of models, a in-house developed custom linear prediction engine, favouring models with fewer parameters, batching requests, and pre-computation and/or caching.