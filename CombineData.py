# This program combines the csv files created from TFIDF.py and getCitations.py into one
# csv file with "Title, Score1, Score2, ..., ScoreN, citations"
# To Run:
# python CombineData.py <File From getCitations.py> <File From TFIDF.py> <Output File>
# Example: python CombineData.py Top100TFIDF.csv Citations.csv Output.csv

import sys
import string
import re

data = {}

with open(sys.argv[2]) as f:
    for line in f:
        text = line.split(',')
        filename = text[1].strip()
        filename = re.sub('\.abs$', '', filename)
        data.update({filename:text[2]})
        
target = open(sys.argv[3], "w")

with open(sys.argv[1]) as f:
    target.write(f.readline())

    for line in f:
        filename = line.split()[0]
        filename = filename.rstrip()
        print filename
        citations = data.get(filename)
        print citations
        line = line.rstrip()
        line = line + citations + "\n"
        print line
        target.write(line)
        
target.close()
