"""
TODO:
colorizer and whitespacer can be the same function run twice
make a "get only words" function

11/18/2018 CHANGES:
* tuple2list converts tuple to 2d array so tag always stays with word
* now formatting html with yattag

"""

class Ghostses:

    def __init__(self, filename):
        """ setup the object """
        self.filename = filename
        self.corpus = None
        self.tokens = None
        self.pos = None

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


# colorize every item that is a part of speech we care about
def colorizer(corpus, tagged, pos, dct ):
    step = 0
    size = len(tagged)
    colorCorpus = corpus
    x = dct[str(pos)]

    for i in x:
        step = 0
        for j in tagged:
            if i == j:
                colorCorpus[step] = """<span class='""" + str(pos) + """'>""" + corpus[step] + """</span>"""
                step = step + 1
            else:
                step = step + 1
    return colorCorpus

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
