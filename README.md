# ghostses

## an overview

*ghostses* is a computationally generated deconstruction/distortion of W.G. Sebald’s *The Rings of Saturn* for two readers with a batterie of instruments (tuning forks, am/fm radios, harmonica/accordion, kitchen timers/bells, and toy percussion). It was commissioned by, and written for, the NYC-based Bent Duo (David Friend and Bill Solomon).

The corpus, (almost all of) Chapter 1 from the Sebald, is separated into multiple layers via a Python program, where each layer shows only one part of speech. Only nouns (printed in red) are visible on the noun layer, for example, and all other text is invisble (though still technically present), ensuring that stacks of multiple layers align properly to reproduce the original text. A reader’s part is created by stacking two or more transparencies on top of the background layer, containing all unused parts of speech from the Sebald and printed on white paper. Performers are free to arrange and rearrange their parts from performance-to-performance.

When performing the piece each player silently reads the entire text of the Sebald “through" the transparencies. When they encounter a colored word on a transparency they may read that word, and (optionally) a few adjacent words, aloud. Simultaneously pairs of colored words cue the beginning and end of instrumental activity, where each instrument is assigned to a different part of speech/layer. Players may begin radio activity, to list only one possible example, when encountering a noun on a transparency while silently reading a page. This radio activity continues until a subsequent noun is encountered. The performance of the piece, then, is dictated both by the individual decisions of each performer as well as their personal, internal reading rate.


## the software

The software to produce *ghostses* is comprised of two interrelated parts:

1. the input corpus is analyzed and regenerated to produce a variety of `html` files (formatted with span class tags)
2. the html files are styled (via `scss`) and rendered to pdf (note: pdf rendering is currently manual)


### analyzing the corpus

The [Ghostses](layer_generator/py/ghostses.py) class reads a text file (the corpus) into memory to prepare for `tokenization` and analysis (in Python 3 via `nltk`). One byproduct of `nltk` tokenization, however, is the removal of whitespace, a critical piece of the corpus required to reassemble the text after analysis. The class attribute `preserveSpaces` allows a programmer to indicate (`True` or `False`) whether whitespace should be preserved during execution of the `constructor method`. If `preserveSpaces` returns `False` `nltk` tokenization proceeds normally, removing and discarding whitespace from the corpus. If `preserveSpaces` returns `True`, as is required to produce a *ghostses* score, a class attribute (`spaces`) is created by `getPOS()` to store the location of all whitespace throughout the corpus.

The class method `colorizer()` identifes whether a corpus item should be rendered visible or invisible for a particular layer. If an item matches the part of speech, set with the argument `partOfSpeech`,`colorizer()` wraps it in a span class which will later be rendered a particular color (for example: all Nouns are red). All non-matching words/items are wrapped in `span class` `whitespace` and will later be rendered invisible.


noun tag Parts of speech categories do not have a uniform number of tags, though, and Catching all nouns requires multiple passes through the corpus (one per tag). For example, there are six possible tags for verbs (`VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`) whereas there are three possible tags for adjectives (`JJ`, `JJR`, `JJS`) a dictionary containing a list of tags for every category

### gulp.js


### making the score
