#usage tests

import nltk
import re

corpus = "corpus.txt"
out = "ghostses_output.txt"

blah = readCorpus(corpus)

newlbah = wordTkzCrps(blah)

corpus = tupleSplitter(newblah)

clean = spaceClnr(corpus[0])

output = colorizer(clean, corpus[1])

outputter(out, output)
