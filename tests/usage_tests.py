# usage example

import nltk
import re

corpus = "score_generator/corpus.txt"
out = "score_generator/words.html"

dctnry={}
dctnry['noun'] = [ 'NN', 'NNP', 'NNPS', 'NNS']
dctnry['adj'] = ['JJ', 'JJR', 'JJS']
dctnry['vrb'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
dctnry['advrb'] = ['RB', 'RBR', 'RBS']

blah = readCorpus(corpus)

newblah = wordTkzCrps(blah)

corpus = tupleSplitter(newblah)

output = colorizer(corpus[0], corpus[1], 'noun', dctnry )

outputer(out, output)

#####

def spaceClnr(corpus):
    newCorpus = []

    for i in corpus:
        if re.search("\W", i) is not None:
            newCorpus.append(i)
            num = num + 1
        else:
            newCorpus.append(" " + i)
            num = num + 1
    return newCorpus
