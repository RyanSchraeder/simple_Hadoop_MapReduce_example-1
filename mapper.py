#!/usr/bin/env python
import sys
import string
import re
import nltk 

from nltk.corpus import stopwords

stops = set(stopwords.words('english'))

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace and make words lowercase
    line = line.strip().lower()

    # remove punctuation
    letters_only = re.sub("[^a-zA-Z", " ", line)
     
    # split the line into words; splits on any whitespace
    words = letters_only.split()

    # organize the sentence with lemmatization

    for word in words: 
        word = lemmatizer.stem(word)
    
    # output tuples (word, 1) of words without any stopwords in tab-delimited format

        print '%s\t%s' % (word, "1")

