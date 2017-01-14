# have to run this line by line

import nltk
import re

corpus = "corpus.txt"
out = "ghostses_output.txt"

blah = readCorpus(corpus)

newlbah = wordTkzCrps(blah)

corpus = tupleSplitter(newblah)

clean = spaceClnr(corpus[0])

output = colorizer(clean, corpus[1])

outputer(out, output)
