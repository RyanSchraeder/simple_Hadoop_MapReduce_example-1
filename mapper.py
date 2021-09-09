#!/usr/bin/env python
import sys
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize

from nltk.corpus import stopwords
stops = set(stopwords.words('english'))

final_words = []

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
# split the line into words; splits on any whitespace
    words = line.split().lower()
# output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stops:
            final_words.append(word)
                print('%s\t%s' % (word, "1"))
# tokenize sentences & words for frequency distribution
sentences = nltk.sent_tokenize(line)
words = nltk.word_tokenize(words)
unique_words = set(words)
print("Total Words After Stopword Removal: ", len(final_words))
print("Total Sentences: ", len(sentences))
print("Total Words: ", len(words))
print("Total unique words: ", len(unique_words))