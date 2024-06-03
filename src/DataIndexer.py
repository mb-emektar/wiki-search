import pyterrier as pt
pt.init()

dataset = pt.get_dataset('irds:dpr-w100')

# Index dpr-w100
indexer = pt.IterDictIndexer('./indices/dpr-w100')

# Indexleme işlemi
index_ref = indexer.index(dataset.get_corpus_iter(), fields=['text', 'title'])