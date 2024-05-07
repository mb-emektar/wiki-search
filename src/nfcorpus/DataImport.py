import pyterrier as pt
pt.init()
dataset = pt.get_dataset('irds:nfcorpus')
# Index nfcorpus
indexer = pt.IterDictIndexer('./indices/nfcorpus')
index_ref = indexer.index(dataset.get_corpus_iter(), fields=['url', 'title', 'abstract'])