"""
TODO:
1. need something that checks for repeated/redundant tags and removes them

~less important~
make a "get only words" function

"""

import itertools
import nltk

class Ghostses:

    def __init__(self, filename):
        """ setup the object """
        self.filename = filename
        self.corpus = None # plaintext of the corpus
        self.whitespace = False # defaults to False, True if tokenization preserves whitespace
        self.tokens = None # tokenized corpus (may contain spaces)
        self.spaces = None # store location of spaces if tokenization preserves whitespace
        self.pos = None # tokenized corpus with parts of speech [token, pos]
        self.colorized = {} # dict to store the colorized parts of speech
        self.words = None # all words from corpus (not yet in use)


    def readCorpus(self):
        """ read the corpus into object """
        f = open(str(self.filename), 'r')
        self.corpus = f.read()


    def getTokens(self, spaces = False):
        """ tokenize corpus """
        if spaces == False:
            self.tokens = nltk.word_tokenize(str(self.corpus))
        elif spaces == True:
            temp = [[nltk.word_tokenize(w), ' '] for w in self.corpus.split()]
            self.tokens = list(itertools.chain(*list(itertools.chain(*temp))))
            self.whitespace = True


    def getPOS(self):
        """ filter out whitespace (if there is any) from tokens
            output whitespace, in original location, to self.spaces
            run parts of speech analysis on non-whitespace tokens
            converts and stores output as 2d list
            [ token, pos ] at self.pos """
        pos_prep = []
        if self.whitespace == False:
            pos = nltk.pos_tag(self.tokens)
            self.pos = list(map(list, pos))
        elif self.whitespace == True:
            size = len(self.tokens)
            self.spaces = [None] * size
            step = 0
            for i in self.tokens:
                if i.isspace() != True:
                    pos_prep.append(i)
                else:
                    self.spaces[step] = i
                step+=1
            pos = nltk.pos_tag(pos_prep)
            self.pos = list(map(list, pos))


    def colorizer(self, spch, dct):
        """ get NLTK tags for part of speech
            find all words that match part of speech and wrap matches in color <span>
            all other words are wrapped in whitespace <span>
            output to dict at self.colorized
        """
        labels = dct
        speech = spch
        size = len(self.pos)
        colorized = [None] * size
        for x in labels[speech]:
            # print("looking for " + x)
            step = 0
            for y in self.pos:
                if y[1] == x:
                    # print("found " + x + " at " + str(step) + " : " + y[0])
                    colorizedToken = "<span class='" + str(speech) + "'>" + str(y[0]) + "</span>"
                    colorized[step] = colorizedToken
                step+=1
        step = 0
        for z in colorized:
            if z == None:
                word = self.pos[step][0]
#                 print(word)
                whitespacedToken = "<span class='whitespace'>" + str(word) + "</span>"
                colorized[step] = whitespacedToken
            step+=1
        self.colorized[str(speech)] = colorized


    def assembler(self, partofspeech):
        """ recombines self.spaces with self.colorized[partofspeech]
            updates self.colorized[partofspeech]
        """
        thepart = partofspeech
        colorized = self.colorized[str(thepart)] # get a local copy of colorized output
        spaces = self.spaces

        step = 0
        for i in spaces:
            if i != " ":
                # print('get a token from self.pos ')
                spaces[step] = colorized[0]
                colorized.pop(0)
            step+=1
        self.colorized[str(thepart)] = spaces


    def renderer(self, partofspeech):

        thepart = str(partofspeech)
        thedir = "../html/"
        body = ''
        head="""
        <!DOCTYPE html>
        <html>
        <head>
        <link rel="stylesheet" href="/css/styles.css" type="text/css"/>
        <link rel="stylesheet" href="/css/print.css" media ="print" type="text/css"/>
        </head>
        <body>
        """

        bottom ="""
        </body>
        </html>
        """

        filename = thedir+thepart+'.html'
        o = open(filename, "w")

        for i in self.colorized[thepart]:
            body+=i
        contents = head+body+bottom
        o.write(contents)
        o.close()
