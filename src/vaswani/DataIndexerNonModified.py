import pyterrier as pt
pt.init()

dataset = pt.get_dataset('irds:vaswani')

# Index vaswani
indexer = pt.IterDictIndexer('./indices/vaswani-nonstem', blocks=True)

# Stopwords ve stemming kapatma
indexer.setProperty("termpipelines", "")

index_ref = indexer.index(dataset.get_corpus_iter(), fields=['text'])