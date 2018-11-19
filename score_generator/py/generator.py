"""
TODO:
1. rewrite getPOs and colorizer to handle spaces if object cares about whitespace
2. rewrite output function

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
        self.tokens = None # tokenized corpus
        self.pos = None # tokenized corpus with parts of speech [token, pos]
        self.whitespace = False # defaults to False, True if tokenization preserves whitespace
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
        """ run parts of speech analysis on tokens
            converts and stores output as 2d list
            [ token, pos ] """
        pos = nltk.pos_tag(self.tokens)
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
                    print("found " + x + " at " + str(step) + " : " + y[0])
                    colorizedToken = "<span class='" + str(speech) + "'>" + str(y[0]) + "</span>"
                    colorized[step] = colorizedToken
                step+=1
        step = 0
        for z in colorized:
            if z == None:
                word = self.pos[step][0]
                print(word)
                whitespacedToken = "<span class='whitespace'>" + str(word) + "</span>"
                colorized[step] = whitespacedToken
            step+=1
        self.colorized[str(speech)] = colorized


#########
#########
#########

# opens the output file, checks to see if text in html tag needs a space before it, writes processed list to output
def outputer(filename, corpus):
    output = []

    o = open(filename, "w") # make a thing that adds which part of speech this is to the extension

    top ="""
    <html>
    <head>
    <link rel="stylesheet" href="/score_generator/css/styles.css" type="text/css"/>
    <link rel="stylesheet" href="/score_generator/css/print.css" media ="print" type="text/css"/>
    </head>
    <body>
    """

    for i in corpus:
        soup = BeautifulSoup(i, "html.parser")
        the_text = soup.get_text()
        if re.search('[^A-Za-z0-9]+', the_text) is not None:
            output.append(str(i))
        else:
            output.append(" " + str(i))

    middle = "".join(output) + "<br/>"

    bottom ="""
    </body>
    </html>
    """

    o.write(top + middle + bottom)
    o.close()
    return output
