#!/usr/bin/env python
import sys
import string
import re 
import nltk 
nltk.download('stopwords')

from nltk.corpus import stopwords
word_tokens = word_tokenize()
import nltk.sentiment.sentiment_analyzer 

stops = set(stopwords.words('english'))

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace and make words lowercase
    line = line.strip().lower()

    # remove punctuation
    letters_only = re.sub("[^a-zA-Z", " ", raw_text)
     
    # split the line into words; splits on any whitespace
    words = line.split()
    
    clean_words = []

    for word in words: 
        if word not in stop_words: 
            clean_words.append(word)

    stemmed_words = []
    # organize the sentence with lemmatization
    word_tokens = word_tokenize(line)

    for word in clean_words: 
        if word in word_tokens: 
           word = lemmatizer.stem(word)
            stemmed_words.append(word)
    
    # output tuples (word, 1) of words without any stopwords in tab-delimited format
    for word in stemmed_words:
        print '%s\t%s' % (word, "1")

