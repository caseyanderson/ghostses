test = Ghostses('corpus_mini.txt')
test.readCorpus()
# test.getTokens()
# test.getPOS()

#refactor the next two lines
dctnry={}
keys = ['noun', 'adj', 'vrb', 'advrb','symb', 'background']

dctnry['noun'] = [ 'NN', 'NNP', 'NNPS', 'NNS']
dctnry['adj'] = ['JJ', 'JJR', 'JJS']
dctnry['vrb'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
dctnry['advrb'] = ['RB', 'RBR', 'RBS']
dctnry['background'] = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'LS', 'MD', 'PDT', 'POS', 'PRP', 'PRP$', 'RP', 'SYM', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRP']
dctnry['symb'] = ['$', "''", '(', ')', ',', '--', '.', ':', "''" ]
