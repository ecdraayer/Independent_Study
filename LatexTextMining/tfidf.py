
import math
import os,re, sys
import io, shutil
from textblob import TextBlob as tb


def tf(word, blob):
    return (float)(blob.words.count(word)) / (float)(len(blob.words))

def n_containing(word, bloblist):
    return (float)(sum(1 for blob in bloblist if word in blob))

def idf(word, bloblist):
    return (float)(math.log(len(bloblist)) / (float)((1 + n_containing(word, bloblist))))

def tfidf(word, blob, bloblist):
    return (float)((float)(tf(word, blob)) * (float)(idf(word, bloblist)))

j = 0

bloblist = []
enc='utf-8'
for filename in os.listdir(sys.argv[1]):
  f = io.open(os.path.join(sys.argv[1], filename), "r", errors='replace')
  bloblist.append(tb(f.read()))
  print f



for i, blob in enumerate(bloblist):
    if i == 0:
        continue
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
    break
