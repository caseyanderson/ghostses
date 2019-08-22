# ghostses

## an overview

ghostses is a computationally generated deconstruction/distortion of W.G. Sebald’s The Rings of Saturn for two readers with a batterie of instruments (tuning forks, am/fm radios, harmonica/accordion, kitchen timers/bells, and toy percussion). It was commissioned by, and written for, the NYC-based Bent Duo (David Friend and Bill Solomon).

The corpus, (almost all of) Chapter 1 from the Sebald, is separated into multiple layers via a Python program, where each layer shows only one part of speech. Only nouns (printed in red) are visible on the noun layer, for example, and all other text is invisble (though still technically present), ensuring that stacks of multiple layers align properly to reproduce the original text. A reader’s part is created by stacking two or more transparencies on top of the background layer, containing all unused parts of speech from the Sebald and printed on white paper. Performers are free to arrange and rearrange their parts from performance-to-performance.

When performing the piece each player silently reads the entire text of the Sebald “through" the transparencies. When they encounter a colored word on a transparency they may read that word, and (optionally) a few adjacent words, aloud. Simultaneously pairs of colored words cue the beginning and end of instrumental activity, where each instrument is assigned to a different part of speech/layer. Players may begin radio activity, to list only one possible example, when encountering a noun on a transparency while silently reading a page. This radio activity continues until a subsequent noun is encountered. The performance of the piece, then, is dictated both by the individual decisions of each performer as well as their personal, internal reading rate.


## the software

The software to produce *ghostses* is comprised of two interrelated parts:

1. the input corpus is analyzed and regenerated to produce a variety of `html` files (formatted with span class tags)
2. the html files are styled (via `scss`) and rendered to pdf (note: pdf rendering is currently manual)


### analyzing the corpus

The `generator` class reads a text file (the input corpus) into memory. The corpus is then ready for tokenization and analysis via `nltk`. One byproduct of `nltk` tokenization, however, is the removal of whitespace, a critical piece of the corpus required to reassemble the text (prior to final rendering). The class attribute `self.preserveSpaces` allows a programmer to indicate (`True` or `False`) whether whitespace should be preserved during execution of the `constructor method`. If `preserveSpaces` returns `False` `nltk` tokenization proceeds as normal and removes whitespace from the corpus. If `preserveSpaces` returns `True`, as in the case of *ghostses*, a separate class attribute (`self.spaces`) is created to store the location of all whitespace throughout the corpus.




### gulp.js

### making the score
