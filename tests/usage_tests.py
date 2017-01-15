# usage example

import nltk
import re

corpus = "score_generator/corpus.txt"
out = "score_generator/words.html"

blah = readCorpus(corpus)

newblah = wordTkzCrps(blah)

corpus = tupleSplitter(newblah)

clean = spaceClnr(corpus[0])

output = colorizer(clean, corpus[1] )

outputter(out, output)
