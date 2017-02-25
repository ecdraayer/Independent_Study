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
rows = tfs.shape[0]
cols = tfs.shape[1]

#convert your matrix to an array to loop over it
mat_array = tfs.toarray()

# get your feature names
fn = tfidf.get_feature_names()
i = 0
for l in mat_array: 
  print token_dict.keys()[i],
  i = i + 1
  print [(fn[x],l[x]) for x in (l*-1).argsort()][:500]

#feature_names = tfidf.get_feature_names()
#print ", ",
#for x in feature_names:
#  print str(x), ", ",
    
#print

#for x in xrange(rows):
#  print token_dict.keys()[x], ", ", 
#  for y in xrange(cols):
#    print tfs[x,y], ", ", 
#  print
#print tfidf.vocabulary_
#print tfs.todense()
