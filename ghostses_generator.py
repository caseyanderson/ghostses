"""
ghostses generator

takes some arbitrary text input, tokenizes into words, assigns parts of speech,
finds only PARTSOFSPEECHWECAREABOUT and capitalizes said in original
outputs contents to file

list of parts of speech tags used in nltk: nltk.help.upenn_tagset()

typesetting via html and css

TODO:
no space before first word!
cleanup
"""

import nltk
import re

filename = 'sebald_chapter_1_RoS.txt'
f = open(filename, 'r')
x =  f.read()

# tokenize to words and then run the parts of speech analysis
tokenized = nltk.word_tokenize(x)
words = nltk.pos_tag(tokenized)

# tokenizer makes a tuple, this splits them and then list castes them, this is so clunky its insane
a,b = zip(*words)
a = list(a)
b = list(b)

# this is a counter and should be refactored to not be necessary (see below)
num = 0

# this checks to see if a word is a part of speech we care about (looks at b) and, if so, capitalizes that word in the other list (a)
for i in b:
    if i == 'NN' or i == 'NNP' or i == 'NNPS' or i == 'NNS':
        a[num] = a[num].upper()
        #make html tags here
    num = num + 1


# if list item does not match punctuation-> no whitespace, else prepend with whitespace.
#need to refactor this, shouldnt need monum...
monum = 0

for i in a:
    if re.match("[,:;?\.()']", i) is not None:
        # print('no match at ' + str(monum) + ', moving on')
        monum = monum + 1
    else:
        # print('match at ' + str(monum))
        a[monum] = " " + i
        monum = monum + 1


# opens the output file and writes the list there
o = open("ghostses_output.txt", "w") # make a thing that adds which part of speech this is to the extension
o.write("".join(a))

o.close()
