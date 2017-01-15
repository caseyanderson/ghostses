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


# colorize every item that is a part of speech we care about
def colorizer(txt, tagged, pos, dct ):
    step = 0
    size = len(tagged)
    colorCorpus = [None] * size
    x = dct[str(pos)]

    for i in x:
        step = 0
        for j in tagged:
            if j != 0:  # make sure this hasnt already been converted
                if j == i: # check to see if the tags match
                    colorCorpus[step] = """<span class='""" + str(pos) + """'>""" + txt[step] + """</span>"""
                    tagged[step] = 0 # skip this next time
                    step = step + 1
                else:
                    colorCorpus[step] = "<span class='whitespace'>" + txt[step] + "</span>"
                    tagged[step] = 0 # skip this one next time
                    step = step + 1
            else:
                step = step + 1
    return colorCorpus


# opens the output file and writes the list there, need to do spacing here also
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

    for i in text:
        text
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
