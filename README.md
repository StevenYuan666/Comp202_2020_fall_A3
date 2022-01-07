# Synonyms Solver
One type of question encountered in the Test of English as a Foreign Language (TOEFL) is the “Synonym Question”, where students are asked to pick a synonym of a word out of a list of alternatives. 

For example:
         1. vexed (Answer: (a) annoyed)
         
        (a) annoyed
        
        (b) amused
        
        (c) frightened
        
        (d) excited
        
Build an intelligent system that can learn to answer questions like this one. In order to do that, the system will approximate the semantic similarity of any pair of words. The semantic similarity between two words is the measure of the closeness of their meanings. For example, the semantic similarity between “car” and “vehicle” is high, while that between “car” and “flower” is low.

In order to answer the TOEFL question, you will compute the semantic similarity between the word you are given and all the possible answers, and pick the answer with the highest semantic similarity to the given word. More precisely, given a word w and a list of potential synonyms s1, s2, s3, s4, we compute the similarities of (w, s1), (w, s2), (w, s3), (w, s4) and choose the word whose similarity to w is the highest.

We will measure the semantic similarity of pairs of words by first computing a semantic descriptor vector of each of the words, and then implement different similarity measures between the two vectors (for example, you will implement a function that computes the cosine similarity).

Given a text with n words denoted by (w1, w2, ..., wn) and a word w, let descw be the semantic descriptor vector of w computed using the text. descw is an n-dimensional vector. The i-th coordinate of descw (i.e. the entry of the vector in position i) is the number of sentences in which both w and wi occur. For efficiency’s sake, for this assignment we will represent semantic descriptor vectors as a dictionaries, not storing the zeros that correspond to words which don’t co-occur with w. 

For example, suppose we are given the following text (an extract from Animal Farm by George Orwell):

*All the habits of Man are evil. And, above all, no animal must ever tyrannise over his own kind. Weak or strong, clever or simple, we are all brothers. No animal must ever kill any other animal. All animals are equal.*

The word “evil” only occurs in the first sentence. Since each word in that sentence occurs in exactly one sentence with the word “evil”, its semantic descriptor vector is: {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'are': 1}

The word “animal” only appears in the second and fourth sentence, but in the fourth sentence it appears twice. Its semantic descriptor vector would be: {'and': 1, 'above': 1, 'all': 1, 'no': 3, 'must': 3, 'ever': 3, 'tyrannise': 1, 'over': 1, 'his': 1, 'own': 1, 'kind': 1, 'kill': 2,  'any': 2, 'other': 2}

We store all words in all-lowercase, since we don’t consider, for example, “Man” and “man” to be different words. We do, however, consider, “animal” and “animals”, or “am” and “is” to be different words. We discard all punctuation.

## Vectors
Given two vectors u = {u1,u2,...,uN} and v = {v1,v2,...,vN}, we can compute the dot product between two vectors using the following formula:

![image](https://user-images.githubusercontent.com/68981504/148491615-9842172a-2975-45f7-829a-f1bc5fa3394b.png)

We cannot apply the formula directly to our semantic descriptors since we do not store the entries which are equal to zero. However, we can still compute the dot product between vectors by only considering the positive entries.

For example, the dot product between the semantic descriptor vectors of “evil” and “animal” is the following:

![image](https://user-images.githubusercontent.com/68981504/148491644-14b5289f-ae8e-4753-8d3a-e4a33f5a72b7.png)

This is because the word “all” is the only key the two semantic descriptor vectors have in common, and in both of dictionaries, “all” maps to the value 1. Similarly, given a vector v = {v1 , v2 , . . . , vN } we can define its norm using the following formula:

![image](https://user-images.githubusercontent.com/68981504/148491679-4f0e94d5-6f81-473f-b80a-e3339e9893a4.png)

Once again we apply the formula to our semantic descriptors considering only the positive entries. For example, the norm of the semantic descriptor vector of “evil” is 2.4494 . . . and the norm of the semantic descriptor vector of “animal” is 6.8556 . . . .

With this in mind we can compute the semantic similarity between two word using a similarity mea- sure. For instance, the cosine similarity measure between two vectors u = {u1, u2, . . . , uN } and v = {v1,v2,...,vN} is defined as:

![image](https://user-images.githubusercontent.com/68981504/148491714-4504b0ef-4148-446b-928d-2a5eba41bcab.png)

So the cosine similarity of “evil” and “animal”, given the semantic descriptors above, is

![image](https://user-images.githubusercontent.com/68981504/148491728-a789a25f-91b1-4179-a3be-4ac75135d22b.png)


Once again we apply the formula to our semantic descriptors considering only the positive entries. For example, the norm of the semantic descriptor vector of “evil” is 2.4494 . . . and the norm of the semantic descriptor vector of “animal” is 6.8556 . . . .
