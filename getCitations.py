# This code uses the scholary python module to retrieve number of citations for each paper
# API can be found here: https://pypi.python.org/pypi/scholarly/0.2
# Search type 1 = citations by "hep-th/<paper number>"
# Search type 2 = Search by paper title
# Search type 0 = No info
# To Run:
# python getCitations.py <Folder with paper abstract files>
# Example: python getCitations.py 2003_abs

import scholarly
import os, sys, re


# Header for csv file
print "Title, Filename, No. of Citations, SearchType"

for filename in os.listdir(sys.argv[1]):
  f = open(os.path.join(sys.argv[1], filename), "r")
  # Find title from abstract file
  data = re.sub( '\s+', ' ', f.read())
  # Title of paper
  title = re.findall(r'Title: (.+?)Author', data)

  # Number of paper
  number = "hep-th/" + filename[:-3]

  # Search by number and search by title
  search_query1 = scholarly.search_pubs_query(number)
  search_query2 = scholarly.search_pubs_query(title[0])

  # Try to search by number first (best way), if that fails
  # search by title instead. If both fail, write no info for
  # citations information
  try:
    TopQuery = next(search_query1)
    searchType = 1
    if hasattr(TopQuery, 'citedby'):
      totalCitations = TopQuery.citedby
    else:
      totalCitations = 0
  except:
    try:
      TopQuery = next(search_query2)
      searchType = 2
      if hasattr(TopQuery, 'citedby'):
        totalCitations = TopQuery.citedby
      else:
        totalCitations = 0
    except:
      searchType = 0
      totalCitations = "NO INFO"


  # Print citations for each paper
  print title[0].replace(',', ''),",",filename,",",totalCitations,",",searchType
