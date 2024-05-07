import pyterrier as pt
pt.init()
dataset = pt.get_dataset('irds:vaswani')
# Index vaswani
indexer = pt.IterDictIndexer('./indices/vaswani', blocks=True)
index_ref = indexer.index(dataset.get_corpus_iter(), fields=['text'])