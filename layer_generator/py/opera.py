"""

in progress refactor and development of ghostses.py for future operas or whatever

"""

from datetime import datetime
from pathlib import Path
import os
import itertools

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

import argparse

class Ghostses:

    def __init__(self, filename):
        """ make a ghostses object
            read the corpus into object
        """
        self.filename = filename
        f = open(str(self.filename), 'r')
        self.corpus = f.read() # plaintext of the corpus


    def getSentences(self):
        """ tokenize corpus by sentence """
        self.sentences = sent_tokenize(score.corpus)        

    
    def getWords(self, preserveSpaces = True):
        """ tokenize corpus sentences by word """
        self.words = []
        for sentence in self.sentences:
            if preserveSpaces == True:
                words = [[word_tokenize(w), ' '] for w in sentence.split()]
                wordList = list(itertools.chain(*list(itertools.chain(*words))))
                if wordList[-1] == ' ':
                    # removes trailing whitespace @ end of sentence if there is any
                    wordList.pop()
                self.words.append(wordList)
            if preserveSpaces == False:
                words = word_tokenize(sentence)
                self.words.append(words)
        self.preserveSpaces = preserveSpaces


#     def getPOS(self):
#         """ filter out whitespace (if there is any) from tokens
#             output whitespace, in original location, to self.spaces
#             run parts of speech analysis on non-whitespace tokens
#             converts and stores output as 2d list
#             [ token, pos ] at self.pos """
#         pos_prep = []
#         if self.preserveSpaces == False:
#             pos = pos_tag(self.tokens)
#             self.pos = list(map(list, pos))
#         elif self.preserveSpaces == True:
#             size = len(self.tokens)
#             self.spaces = [None] * size
#             step = 0
#             for i in self.tokens:
#                 if i.isspace() != True:
#                     pos_prep.append(i)
#                 else:
#                     self.spaces[step] = i
#                 step+=1
#             pos = pos_tag(pos_prep)
#             self.pos = list(map(list, pos))
