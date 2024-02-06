
# The following program finds all unique words in the Bible
## note that the text file does not currently work.


from string import maketrans
import pandas as pd
word_freq = {}

infile="c:/temp/AV1611.txt"

word_list = open(infile, "r").read().split()
ttt='!"#$%&()*+,./:;<=>?@[\\]^_`{|}~0123456789'
for word in word_list:
    word = word.translate(maketrans("",""),ttt )
    if word.startswith('-'):
        word = word.replace('-','')
    if len(word):
        word_freq[word] = word_freq.get(word, 0) + 1
keys = sorted(word_freq.keys())
x=pd.DataFrame(keys)
x.to_pickle('uniqueWordsBible.pkl')