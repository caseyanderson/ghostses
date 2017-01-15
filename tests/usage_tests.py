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

//

care = ['noun', 'adj', 'vrb','advrb']
dctnry = { 'noun':  ['NN', 'NNP', 'NNPS', 'NNS'], 'adj': ['JJ', 'JJR', 'JJS'], 'vrb': ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'], 'advrb': ['RB', 'RBR', 'RBS'] }

#step = 0
#care = 'noun'

x = dctnry[pos]

for i in x: #
    step = 0
    for j in corpus[1]:
        if j == i:
            #print(corpus[0][step])
            txt[step] = """<span class='""" + pos + """'>""" + txt[step] + """</span>"""
            step = step + 1
        else:
#            print('NO MATCH')
            txt[step] = "<span class='whitespace'>" + txt[step] + "</span>"
            step = step + 1



    # for j in corpus[1]:
    #     if j == i:
    #         corpus[0][step] = """<span class='""" + pos + """'>""" + corpus[0][step] + """</span>"""
    #         step = step + 1
    #     else:
    #         corpus[0][step] = "<span class='whitespace'>" + corpus[0][step] + "</span>"
    #         step = step + 1

outputter(out, corpus[0])

def outputter(filename, text):
    o = open(filename, "w") # make a thing that adds which part of speech this is to the extension

    top ="""
    <html>
    <head>
    <link rel="stylesheet" href="styles.css" type="text/css"/>
    <link rel="stylesheet" href="print.css" media ="print" type="text/css"/>
    </head>
    <body>
    """

    middle = "".join(text) + "<br/>"

    bottom ="""
    </body>
    </html>
    """

    o.write(top + middle + bottom)
    o.close()
