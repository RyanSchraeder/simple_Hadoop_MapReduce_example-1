#!/usr/bin/env python
import sys
import pandas as pd
import numpy as np
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import inaugural
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('inaugural')
nltk.download('punkt')

stops = set(stopwords.words('english'))

corpus = inaugural.raw('1789-Washington.txt')

sentences = nltk.sent_tokenize(corpus)
print("Total Sentences: ", len(sentences))

words = nltk.word_tokenize(corpus)
print("Total Words: ", len(words))

unique_words = set(words)
print("Total unique words: ", len(unique_words))

final_words = defaultdict(list)

# get all lines from text
for line in sentences:

# remove leading and trailing whitespace
    line = sentences.lower()

# split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stops:
            print('%s\t%s' % (word, "1"))
            final_words.append(word)
print(final_words)