# usage example

import nltk
import re
from bs4 import BeautifulSoup

corpus = "score_generator/corpus.txt"
out = "score_generator/words.html"

dctnry={}
dctnry['noun'] = [ 'NN', 'NNP', 'NNPS', 'NNS']
dctnry['adj'] = ['JJ', 'JJR', 'JJS']
dctnry['vrb'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
dctnry['advrb'] = ['RB', 'RBR', 'RBS']
dctnry['rest'] = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'LS', 'MD', 'PDT', 'POS', 'PRP', 'PRP$', 'RP', 'SYM', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRP']
dctnry['symb'] = ['$', "''", '(', ')', ',', '--', '.', ':', "''" ]

blah = readCorpus(corpus)

newblah = wordTkzCrps(blah)

corpus = tupleSplitter(newblah)

output = colorizer(corpus[0], corpus[1], 'noun', dctnry )

allhtml = whitespacer(output)

final = outputer(out, allhtml)
