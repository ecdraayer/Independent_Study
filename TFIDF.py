# This program applies TFIDF scoring technique to the research papers
# Modeled From:http://www.cs.duke.edu/courses/spring14/compsci290/assignments/lab02.html
# Other useful tutorials:
# http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/
# https://gist.github.com/anabranch/48c5c0124ba4e162b2e3
# http://www.markhneedham.com/blog/2015/02/15/pythonscikit-learn-calculating-tfidf-on-how-i-met-your-mother-transcripts/
# To Run:
# python TFIDF.py <Directory Contianing Papers> > OutputFile
# Example python TFIDF.py Detexed_2003_Papers > Top100TFIDF.csv

import nltk
import os, sys, re
import string
import numpy as np

from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from pandas import DataFrame
token_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
  stemmed = []
  for item in tokens:
    stemmed.append(stemmer.stem(item))
  return stemmed
  
def tokenize(text):
  tokens = nltk.word_tokenize(text)
  stems = stem_tokens(tokens, stemmer)
  return stems  

for filename in os.listdir(sys.argv[1]):
  ResearchPaper = open(os.path.join(sys.argv[1], filename), 'r')
  text = ResearchPaper.read()
  lowers = text.lower()
  no_punctuation = lowers.translate(None, string.punctuation)
  token_dict[filename] = no_punctuation
    
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())


#convert your matrix to an array to loop over it
mat_array = tfs.toarray()

# get your feature names
fn = tfidf.get_feature_names()

# k top words from Tfidf
k = 100

# Print Labels: Filename, word1, word2, ... Citations
print "Filename,",
for i in range(k):
  string = "Score"+str(i+1)
  print string,",",

print "Citations"

words = []
i = 0
for l in mat_array: 
  print token_dict.keys()[i], ", ",
  stuff = [(fn[x],l[x]) for x in (l*-1).argsort()][:k]
  i += 1
  for rows in stuff:
    print rows[1], ", ",

  print "" 
  
