#!/usr/bin/env python
import sys
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize

from nltk.corpus import stopwords
stops = set(stopwords.words('english'))

# get all lines from stdin
for line in sys.stdin:

# remove leading and trailing whitespace
    line = line.strip().lower()

# split the line into words; splits on any whitespace
    words = line.split().lower()

    # tokenize sentences & words for frequency distribution
    sentences = nltk.sent_tokenize(line)
    print("Total Sentences: ", len(sentences))

    words = nltk.word_tokenize(words)
    print("Total Words: ", len(words))

    unique_words = set(words)
    print("Total unique words: ", len(unique_words))

    final_words = []
    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stopwords:
        final_words.append(word)
        
        print(" --- Top Words After Removing Stopwords --- ")
        print('%s\t%s' % (word, "1"))
        print("Total Words After Stopword Removal: ", len(final_words))
        print("Top Word by Frequency: ", final_words.value_counts().nlargest(1))
        