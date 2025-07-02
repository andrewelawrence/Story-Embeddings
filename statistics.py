"""
- `len(text.split())` or `nltk.word_tokenize()` and `statistics.mean([len(word) for word in words])`
- `nltk.sent_tokenize()` or `spacy.sentencizer = nlp.add_pipe("sentencizer")`
- `text.split('\n')`
- `text.split('\n\n')`
- `len(set(words)) / len(words)`
- `nltk.ngrams()` or `collections.Counter`
- `lexical_diversity` package
- `collections.Counter(words)`
- `textstat` package
- `nltk.pos_tag()` or `spacy` POS tagging
- `spacy.load("en_core_web_sm").ents` or `nltk.ne_chunk()`
- `string.printable`, `unicodedata` module
- `scipy.stats.pearsonr()` or `numpy.corrcoef()`
- `transformers.AutoTokenizer.from_pretrained()`
- `numpy.percentile()`, IQR calculations
"""
