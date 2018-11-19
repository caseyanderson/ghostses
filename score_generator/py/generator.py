"""
TODO:
colorizer and whitespacer can be the same function run twice
make a "get only words" function

11/18/2018 CHANGES:
* now formatting html with yattag

"""


class Ghostses:

    def __init__(self, filename):
        """ setup the object """
        self.filename = filename
        self.corpus = None # plaintext of the corpus
        self.tokens = None # tokenized version of the corpus
        self.pos = None # textenized version of the corpus with parts of speech [word, pos]
        self.colorized = {} # dict to store the colorized parts of speech 


    def readCorpus(self):
        """ read the corpus into object """
        f = open(str(self.filename), 'r')
        self.corpus = f.read()


    def getTokens(self):
        """ tokenize corpus """
        self.tokens = nltk.word_tokenize(str(self.corpus))


    def getPOS(self):
        """ run parts of speech analysis on tokens
            converts and stores output as 2d list
            [ token, pos ] """
        pos = nltk.pos_tag(self.tokens)
        self.pos = list(map(list, pos))


    def colorizer(self, spch, dct):
        labels = dct
        speech = spch
        size = len(self.pos)
        colorized = [None] * size
        for x in labels[speech]:
            print("looking for " + x)
            step = 0
            for y in self.pos:
                if y[1] == x:
                    print("found " + x + " at " + str(step) + " : " + y[0])
                    colorizedToken = "<span class='" + str(speech) + "'>" + str(y[0]) + "</a>"
                    colorized[step] = colorizedToken
                step+=1
        self.colorized[str(speech)] = colorized


# everything not colorized by colorizer is whitespace
def whitespacer(corpus):
    output = []

    for i in corpus:
        if re.search("<[^<>]+>", i) is not None:
            output.append(i)
        else:
            output.append("""<span class='whitespace'>""" + i + """</span>""")
    return output

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
