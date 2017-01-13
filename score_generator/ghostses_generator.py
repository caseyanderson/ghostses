"""
ghostses generator


1. reads arbitrary text input
2. tokenizes text into words (followed by quick spacing fix)
3. assigns parts of speech
4. finds parts of speech we care about and colors said in original
5. everything else is invisible
6. outputs contents to a file

list of parts of speech tags used in nltk: nltk.help.upenn_tagset()

TODO:
no space before first word!
cleanup
"""

import nltk
import re

filename = 'score_generator/corpus.txt'
f = open(filename, 'r')
x =  f.read()

# tokenize to words and then run the parts of speech analysis
tokenized = nltk.word_tokenize(x)
words = nltk.pos_tag(tokenized)

# tokenizer makes a tuple, this splits them and then list castes them, this is so clunky its insane
a,b = zip(*words)
a = list(a)
b = list(b)


# if an item contains any non-alphanumeric characters it does not get prepended with a space
num = 0

for i in a:
    if re.match("\W", i) is not None:
        num = num + 1
    else:
        a[num] = " " + a[num]
        num = num + 1

monum = 0

# colorizes text if it is a part of speech we care about, otherwise opacity of text is 0 (i.e. invisible)
for i in b:
    # if i == 'NN' or i == 'NNP' or i == 'NNPS' or i == 'NNS':
    # if i == 'JJ' or i == 'JJR' or i == 'JJS':
    if i == 'VB' or i == 'VBD' or i == 'VBG' or i == 'VBN' or i == 'VBP' or i == 'VBZ':
        a[monum] = "<span class='vrb'>" + a[monum] + "</span>"
        monum = monum + 1
    else:
        a[monum] = "<span class='whitespace'>" + a[monum] + "</span>"
        monum = monum + 1

# opens the output file and writes the list there
o = open("score_generator/ghostses_output.txt", "w") # make a thing that adds which part of speech this is to the extension
o.write("".join(a))

o.close()
