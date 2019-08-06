"""
ghostses (score generator) by Casey Anderson

usage: python3 generator.py --ws True

TODO:
1. need something that checks for repeated/redundant tags and removes them

"""

from datetime import datetime
from pathlib import Path
import os
import itertools
import nltk
import argparse

class Ghostses:

    def __init__(self, filename):
        """ setup a ghostses object """
        self.filename = filename
        self.corpus = None # plaintext of the corpus
        self.whitespace = False # defaults to False, True if tokenization preserves whitespace
        self.tokens = None # tokenized corpus (may contain spaces)
        self.spaces = None # store location of spaces if tokenization preserves whitespace
        self.pos = None # tokenized corpus with parts of speech [token, pos]
        self.colorized = {} # dict to store the colorized parts of speech


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


    def proto(self):
        """ makes a prototyping directory, labeled with corpus stem + date and time
            changes directories into stem-datetime
        """
        thedir = "/Users/cta/werk/ghostses/layer_generator/html/"

        proto = datetime.now().strftime("%m%d%Y_%H%M%S")
        name = Path(self.filename).stem
        path = "".join([str(name), "_", str(proto)])

        os.chdir(thedir)

        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
        os.chdir(path)


    def renderer(self, partofspeech):

        thepart = str(partofspeech)
        body = ''
        head="""
        <!DOCTYPE html>
        <html>
        <head>
        <link rel="stylesheet" href="../../css/styles.css" type="text/css"/>
        <link rel="stylesheet" href="../../css/print.css" media ="print" type="text/css"/>
        </head>
        <body>
        """

        bottom ="""
        </body>
        </html>
        """

        filename = thepart+'.html'
        o = open(filename, "w")

        for i in self.colorized[thepart]:
            body+=i
        contents = head+body+bottom
        o.write(contents)
        o.close()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--crps", type=str, default="../../corpora/ch1_RoS/ch1_RoS_edited.txt",
                        help="the corpus")
    parser.add_argument("--ws", type=bool, default=False,
                        help="preserve whitespace")
    args = parser.parse_args()

    ## setup

    score = Ghostses(args.crps) # make the score text object, set the corpus filepath
    score.readCorpus() # read the corpus into object
    score.getTokens(spaces=args.ws) # get tokens and preserve spaces
    score.getPOS() # perform parts of speech analysis on non-whitespace tokens
    score.proto() # make the prototype dir

    # make the colorizer dictionary

    dctnry={}
    keys = ['noun', 'adj', 'vrb', 'advrb','symb', 'background']

    # possible tags per each part of speech category

    dctnry['noun'] = [ 'NN', 'NNP', 'NNPS', 'NNS']
    dctnry['adj'] = ['JJ', 'JJR', 'JJS']
    dctnry['vrb'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    dctnry['advrb'] = ['RB', 'RBR', 'RBS']
    dctnry['background'] = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'LS', 'MD', 'PDT', 'POS', 'PRP', 'PRP$', 'RP', 'SYM', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRP']
    dctnry['symb'] = ['$', "''", '(', ')', ',', '--', '.', ':', "''" ]

    # make all of the layers, output to proto dir

    for i in keys:
        print('making ' + str(i))
        score.colorizer(str(i), dctnry) # add html tags
        score.assembler(str(i)) # combine spaces with processed list
        score.renderer(str(i)) # format and write the html file

if __name__ == '__main__':
    main()
