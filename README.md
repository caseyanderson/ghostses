# ghostses

## an overview

*ghostses* is a computationally generated deconstruction/distortion of W.G. Sebald’s *The Rings of Saturn* for two readers with a batterie of instruments (tuning forks, am/fm radios, harmonica/accordion, kitchen timers/bells, and toy percussion). It was commissioned by, and written for, the NYC-based Bent Duo (David Friend and Bill Solomon).

The corpus, (almost all of) Chapter 1 from the Sebald, is separated into multiple layers via a Python program, where each layer shows only one part of speech. Only nouns (printed in red) are visible on the noun layer, for example, and all other text is invisble (though still technically present), ensuring that stacks of multiple layers align properly to reproduce the original text. A reader’s part is created by stacking two or more transparencies on top of the background layer, containing all unused parts of speech from the Sebald and printed on white paper. Performers are free to arrange and rearrange their parts from performance-to-performance.

When performing the piece each player silently reads the entire text of the Sebald “through" the transparencies. When they encounter a colored word on a transparency they may read that word, and (optionally) a few adjacent words, aloud. Simultaneously pairs of colored words cue the beginning and end of instrumental activity, where each instrument is assigned to a different part of speech/layer. Players may begin radio activity, to list only one possible example, when encountering a noun on a transparency while silently reading a page. This radio activity continues until a subsequent noun is encountered. The performance of the piece, then, is dictated both by the individual decisions of each performer as well as their personal, internal reading rate.


## the software

The software to produce *ghostses* is comprised of two interrelated parts:

1. the input corpus is analyzed and regenerated to produce a variety of `html` files (formatted with span class tags)
2. the html files are styled (via `scss`) and rendered to pdf (pdf rendering is currently manual)

*Note*: I currently use gulp.js w/ browser-sync (and some other plugins) to generate the `.css` from `.scss`, see [gulpfile.js](https://github.com/caseyanderson/ghostses/blob/master/gulpfile.js) for more info


### analyzing and styling the corpus

The [Ghostses](layer_generator/py/ghostses.py) class reads a text file (the corpus) into memory to prepare for `tokenization` and analysis (in Python 3 via `nltk`). One byproduct of `nltk` tokenization, however, is the removal of whitespace, a critical piece of the corpus required to reassemble the text after analysis. The class attribute `preserveSpaces` allows a programmer to indicate (`True` or `False`) whether whitespace should be preserved during execution of the `constructor method`. If `preserveSpaces` returns `False` `nltk` tokenization proceeds normally, removing and discarding whitespace from the corpus. If `preserveSpaces` returns `True`, as is required to produce a *ghostses* score, a class attribute (`spaces`) is created by `getPOS()` to store the location of all whitespace throughout the corpus.

The class method `colorizer()` identifes whether a corpus item should be rendered visible or invisible for a particular layer. If an item and its tag (stored in `self.pos`) matches the desired part of speech, set with the argument `partOfSpeech`,`colorizer()` wraps it in a `span class` which will later be rendered a particular color (for example: all nouns are red). All non-matching words/items are wrapped in `span class` `whitespace` and will later be rendered invisible.

Parts of speech categories often have more than one tag, though, so catching all verbs, for example, requires more than one pass through the corpus (one per tag). Additionally, there is not a uniform number of tags per category. For example: there are six possible tags for verbs (`VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`) whereas there are three possible tags for adjectives (`JJ`, `JJR`, `JJS`). `colorizer()` expects to be passed a dictionary containing keys for each category (example key: `noun`) with a list containing the number of tags affiliated with that category (example list for the key `noun`: `['NN','NNP','NNPS','NNS']`).

A dictionary of all tags, organized by categories (noun, adjective, verb, adverb, background [unused portions of the text e.g. articles], and symbols [punctuation]) is created (`posKeysTags` [here](https://github.com/caseyanderson/ghostses/blob/6c117bbb8a26741df9531791ff66a92cb8c3b7cb/layer_generator/py/ghostses.py#L175-L187)) to feed `colorizer()` with the appropriate quantity of tags per parts of speech category, enabling one to generate a `noun` layer with the following: `score.colorizer('noun', posKeysTags)`. In `main()` we generate all layers at once with a [for loop](https://github.com/caseyanderson/ghostses/blob/6c117bbb8a26741df9531791ff66a92cb8c3b7cb/layer_generator/py/ghostses.py#L190-L194).

The class method `assembler()` reconstructs the corpus by combining a tagged layer with `self.spaces`, ensuring that words are in the same location on each page regardless of how they are styled. The class method `proto()` creates a folder, labeled with the date, time, and corpus name, to easily allow for comparisons between generations (hence `proto()` or `prototype`). Finally, `renderer()` creates the output `html` files (one for every layer) and saves them to the directory produced by `proto()`.


### making the score

Current procedure for creating the score:

1. open all `.html` files in the directory created by `proto()` with a browser (Firefox, for example)
2. `File` > `Print` > `Save as PDF` (for every `.html` file)
3. print every `.pdf` file with the **same** color printer
    1. print `background.pdf` onto 8.5x11 white paper
    2. print all other files onto 8.5x11 clear transparencies

*Note* in the future converting `.html` to `.pdf` will be automatic

**FYI** one copy of a full set of ghostses costs approximately $100 each (it's a duo so $100 * 2 = $200 total) to produce (whoops, heh). Owning a color printer capable of printing onto transparencies *drastically* reduces the cost to produce
