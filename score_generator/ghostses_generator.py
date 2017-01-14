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
no space before first word! (fixing this manually right now)
cleanup
"""

import nltk
import re

# reads a textfile
def readCorpus(filename):
    f = open(str(filename), 'r')
    x = f.read()
    return x

# tokenize to words and then run the parts of speech analysis
def wordTkzCrps(corpus):
    tokenized = nltk.word_tokenize(str(corpus))
    words = nltk.pos_tag(tokenized)
    return words

# pos makes a tuple, this splits them and then list castes them, this is so clunky its insane
def tupleSplitter(pos):
    a,b = zip(*pos)
    a = list(a)
    b = list(b)
    return a, b

# if an item contains any non-alphanumeric characters it does not get prepended with a space
def spaceClnr(corpus):
    num = 0

    for i in corpus:
        if re.match("\W", i) is not None:
            num = num + 1
        else:
            corpus[num] = " " + corpus[num]
            num = num + 1
        return corpus

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
def outputter(filename, text):
    o = open(filename, "w") # make a thing that adds which part of speech this is to the extension
    o.write("".join(text))

    o.close()

##########

# if i == 'NN' or i == 'NNP' or i == 'NNPS' or i == 'NNS':
# if i == 'JJ' or i == 'JJR' or i == 'JJS':
# if i == 'VB' or i == 'VBD' or i == 'VBG' or i == 'VBN' or i == 'VBP' or i == 'VBZ':
# if i == 'RB' or i == 'RBR' or i == 'RBS':
