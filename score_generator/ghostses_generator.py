"""
ghostses generator

1. reads arbitrary text input
2. tokenizes text into words (followed by quick spacing fix)
3. assigns parts of speech
4. finds parts of speech we care about and colors said in original
5. everything else is invisible
6. outputs contents to a file

list of parts of speech tags used in nltk: nltk.help.upenn_tagset()

TODO:
make into class
"""

import nltk
import re

# reads a textfile
def readCorpus(filename):
    f = open(str(filename), 'r')
    x = f.read()
    return x

# tokenize to words and then run the parts of speech analysis, outputs a tuple
def wordTkzCrps(corpus):
    tokenized = nltk.word_tokenize(str(corpus))
    words = nltk.pos_tag(tokenized)
    return words

# splits a tuple list castes the output
def tupleSplitter(pos):
    a,b = zip(*pos)
    a = list(a)
    b = list(b)
    return a, b

# if an item contains any non-alphanumeric characters it does not get a space
def spaceClnr(corpus):
    num = 1 # skips first word

    for i in corpus:
        if re.match("\W", i) is not None:
            # print("not a match: " + str(i) + " num is " + num)
            num = num + 1
        else:
            corpus[num] = " " + corpus[num]
            num = num + 1
    return corpus

# colorize every item that is a part of speech we care about
def colorizer(txt, pos ):
    step = 0

    for i in pos:
        if i == 'NN' or i == 'NNP' or i == 'NNPS' or i == 'NNS':

            txt[step] = "<span class='noun'>" + txt[step] + "</span>"
            step = step + 1
        else:
            txt[step] = "<span class='whitespace'>" + txt[step] + "</span>"
            step = step + 1
    return txt

# opens the output file and writes the list there
def outputer(filename, text):
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

##########

# if i == 'NN' or i == 'NNP' or i == 'NNPS' or i == 'NNS':
# if i == 'JJ' or i == 'JJR' or i == 'JJS':
# if i == 'VB' or i == 'VBD' or i == 'VBG' or i == 'VBN' or i == 'VBP' or i == 'VBZ':
# if i == 'RB' or i == 'RBR' or i == 'RBS':
