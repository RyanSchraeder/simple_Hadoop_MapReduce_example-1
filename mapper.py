#!/usr/bin/env python
import sys
import string 
import nltk 
nltk.download('stopwords')
from nltk.corpus import stopwords
import nltk.sentiment.sentiment_analyzer 

stops = set(stopwords.words('english'))
positive_words = ['good', 'happy', 'excited', 'amazing', 'relieved']
    

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace and make words lowercase
    line = line.strip().lower()
  
    # split the line into words; splits on any whitespace
    words = line.split()

    # analyze for positive sentiment 
    analysis = nltk.sentiment.util.extract_unigram_feats(words, positive_words)

    # output tuples (word, 1) of words without any stopwords in tab-delimited format
    for word in words:
        if word not in stops:
        print '%s\t%s' % (word, "1")
        print('\n** Positive Sentiment For Each Word **\n')
        print(analysis)

