import io
import nltk
import pandas as pd 
import numpy as np

# Load in static sample data
colnames = ['Title', 'Submission Score', 'Submission ID', 'Submission URL', 'Prices', 'Seller']
# df = pd.read_csv('../data/comment_data_sample.csv')

'''
LIST COMPREHENSIONS WIN COMPUTE TIME 

$ python2.6 -m timeit '[x.lower() for x in ["A","B","C"]]'
1000000 loops, best of 3: 1.03 usec per loop
$ python2.6 -m timeit '[x.upper() for x in ["a","b","c"]]'
1000000 loops, best of 3: 1.04 usec per loop

$ python2.6 -m timeit 'map(str.lower,["A","B","C"])'
1000000 loops, best of 3: 1.44 usec per loop
$ python2.6 -m timeit 'map(str.upper,["a","b","c"])'
1000000 loops, best of 3: 1.44 usec per loop

$ python2.6 -m timeit 'map(lambda x:x.lower(),["A","B","C"])'
1000000 loops, best of 3: 1.87 usec per loop
$ python2.6 -m timeit 'map(lambda x:x.upper(),["a","b","c"])'
1000000 loops, best of 3: 1.87 usec per loop
'''

# array lowercase conversion: map(str.lower, ["A","B","C"])
sample_array = ['A', 'B', 'SOLD']
sample_array2 = ['A', 'B', 'naw']

# Item sold indicator
def item_sold(comment_array):
    comment_array = [x.lower() for x in comment_array] # lower ALL
    if any('sold' in x for x in comment_array):
        return 'SOLD'
    else:
        return 'AVAILABLE'

# Extract brand
brand_corpus = []
with io.open('./data/brand_corpus.txt', encoding='latin-1') as myfile:
    for i in myfile.readlines():
        brand_corpus.append(i)
brand_corpus = [x[:-1] for x in brand_corpus] # delete newline \n 
brand_corpus = [x.lower() for x in brand_corpus] # lower ALL

print(brand_corpus)

def brand_extractor(submission_text, comment_array):
    return 2