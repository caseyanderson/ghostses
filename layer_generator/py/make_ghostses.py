#!/usr/bin/env python3

'''
make ghostses, fall 2018
Casey anderson

to run: python3 make_ghostses.py --ws True

'''

from generator import *
import argparse


if __name__ == '__main__':

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


    # makethe colorizer dictionary

    dctnry={}
    keys = ['noun', 'adj', 'vrb', 'advrb','symb', 'background']


    # possible tags per each part of speech category

    dctnry['noun'] = [ 'NN', 'NNP', 'NNPS', 'NNS']
    dctnry['adj'] = ['JJ', 'JJR', 'JJS']
    dctnry['vrb'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    dctnry['advrb'] = ['RB', 'RBR', 'RBS']
    dctnry['background'] = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'LS', 'MD', 'PDT', 'POS', 'PRP', 'PRP$', 'RP', 'SYM', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRP']
    dctnry['symb'] = ['$', "''", '(', ')', ',', '--', '.', ':', "''" ]


    # make all of the layers, output to /layer_generator/html/

    for i in keys:
        print('making ' + str(i))
        score.colorizer(str(i), dctnry) # add html tags
        score.assembler(str(i)) # combine spaces with processed list
        score.renderer(str(i)) # format and write the html file
