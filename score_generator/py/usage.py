# making ghostses


## setup

score = Ghostses('corpus.txt') # make the score text object, set the corpus filepath
score.readCorpus() # read the corpus into object
score.getTokens(spaces=True) # get tokens and preserve spaces
score.getPOS() # perform parts of speech analysis on non-whitespace tokens


# makethe colorizer dictionary
dctnry={}
keys = ['noun', 'adj', 'vrb', 'advrb','symb', 'background']

dctnry['noun'] = [ 'NN', 'NNP', 'NNPS', 'NNS']
dctnry['adj'] = ['JJ', 'JJR', 'JJS']
dctnry['vrb'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
dctnry['advrb'] = ['RB', 'RBR', 'RBS']
dctnry['background'] = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'LS', 'MD', 'PDT', 'POS', 'PRP', 'PRP$', 'RP', 'SYM', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRP']
dctnry['symb'] = ['$', "''", '(', ')', ',', '--', '.', ':', "''" ]

for i in keys:
    print('making ' + str(i))
    score.colorizer(str(i), dctnry)
    score.assembler(str(i))
    score.renderer(str(i))
