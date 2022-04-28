"""
ghostses (score generator) by Casey Anderson

usage: python3 ghostses.py --ws True

note: this class has been archived,
new work that builds on ghostses is
currently in opera.py and will
eventually be in a new repo

"""

from datetime import datetime
from pathlib import Path
import os
import itertools
import nltk
import argparse

class Ghostses:

    def __init__(self, filename):
        """ make a ghostses object
            read the corpus into object
        """
        self.filename = filename
        f = open(str(self.filename), 'r')
        self.corpus = f.read() # plaintext of the corpus


    def getTokens(self, preserveSpaces = False):
        """ tokenize corpus """
        if preserveSpaces == False:
            self.tokens = nltk.word_tokenize(str(self.corpus))
        elif preserveSpaces == True:
            temp = [[nltk.word_tokenize(w), ' '] for w in self.corpus.split()]
            self.tokens = list(itertools.chain(*list(itertools.chain(*temp))))
        self.preserveSpaces = preserveSpaces


    def getPOS(self):
        """ filter out whitespace (if there is any) from tokens
            output whitespace, in original location, to self.spaces
            run parts of speech analysis on non-whitespace tokens
            converts and stores output as 2d list
            [ token, pos ] at self.pos """
        pos_prep = []
        if self.preserveSpaces == False:
            pos = nltk.pos_tag(self.tokens)
            self.pos = list(map(list, pos))
        elif self.preserveSpaces == True:
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


    def colorizer(self, partOfSpeech, tags):
        """ get NLTK tags for part of speech
            find all words that match part of speech and wrap matches in color <span>
            all other words are wrapped in whitespace <span>
            output to dict at self.colorized
        """
        self.colorized = {} # make the output dictionary
        labels = tags
        speech = partOfSpeech
        size = len(self.pos)
        colorized = [None] * size
        for x in labels[speech]:
            step = 0
            for y in self.pos:
                if y[1] == x:
                    colorizedToken = "<span class='" + str(speech) + "'>" + str(y[0]) + "</span>"
                    colorized[step] = colorizedToken
                step+=1
        step = 0
        for z in colorized:
            if z == None:
                word = self.pos[step][0]
                whitespacedToken = "<span class='whitespace'>" + str(word) + "</span>"
                colorized[step] = whitespacedToken
            step+=1
        self.colorized[str(speech)] = colorized


    def assembler(self, partOfSpeech):
        """ recombines self.spaces with self.colorized[partofspeech]
            updates self.colorized[partofspeech]
        """
        thepart = partOfSpeech
        colorized = self.colorized[str(thepart)] # get a local copy of colorized output
        spaces = self.spaces

        step = 0
        for i in spaces:
            if i != " ":
                spaces[step] = colorized[0]
                colorized.pop(0)
            step+=1
        self.colorized[str(thepart)] = spaces


    def proto(self):
        """ makes a prototyping directory, labeled with corpus stem-datetime
            changes directories into stem-datetime
        """
        #thedir = "/Users/cta/werk/ghostses/layer_generator/html/"
        thedir = "/home/cta/ghostses/layer_generator/html/"

        proto = datetime.now().strftime("%m%d%Y_%H%M%S")
        name = Path(self.filename).stem
        path = "".join([str(name), "-", str(proto)])

        os.chdir(thedir)

        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
        os.chdir(path)


    def renderer(self, partOfSpeech):

        pos = str(partOfSpeech)
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

        filename = pos+'.html'
        o = open(filename, "w")

        for i in self.colorized[pos]:
            body+=i
        contents = head+body+bottom
        o.write(contents)
        o.close()


def main():

    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--crps", type=str, default="/home/cta/ghostses/corpora/ch1_RoS/ch1_RoS_edited.txt",
                        help="the corpus")
    parser.add_argument("--ws", type=bool, default=False,
                        help="preserve whitespace")
    args = parser.parse_args()

    # setup
    score = Ghostses(args.crps) # make score object, set corpus filepath, read corpus into object
    score.getTokens(preserveSpaces=args.ws) # get tokens and preserve spaces
    score.getPOS() # perform parts of speech analysis on non-whitespace tokens
    score.proto() # make the prototype dir

    # make the posKeysTags dictionary
    posKeysTags={}
    keys = ['noun', 'adjective', 'verb', 'adverb', 'background', 'symbol']
    tags = [
        ['NN','NNP','NNPS','NNS'],
        ['JJ','JJR','JJS'],
        ['VB','VBD','VBG','VBN','VBP','VBZ'],
        ['RB','RBR','RBS','WRB'],
        ['CC','CD','DT','EX','FW','IN','LS','MD','PDT','POS','PRP','PRP$','RP','TO','UH','WDT','WP','WP$'],
        ['$',"''",'(',')',',','--','.',':','SYM',"``"]
    ]

    for x, y in zip(keys, tags):
        posKeysTags[x] = y

    # make all of the layers, output to proto dir
    for i in keys:
        print('making ' + str(i))
        score.colorizer(str(i), posKeysTags) # add html tags
        score.assembler(str(i)) # combine spaces with processed list
        score.renderer(str(i)) # format and write the html file

if __name__ == '__main__':
    main()
