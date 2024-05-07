import pyterrier as pt
from pyterrier.measures import *
pt.init()
dataset = pt.get_dataset('irds:dpr-w100/natural-questions/dev')
index_ref = "/Users/berkguler/Downloads/older/master/CENG 596 - Info Retrieval/project/indices/dpr-w100"
pipeline = pt.BatchRetrieve(index_ref, wmodel='BM25')
# (optionally other pipeline components)
print("in here1")
result = pt.Experiment(
    [pipeline],
    dataset.get_topics('text'),
    dataset.get_qrels(),
    [MAP, nDCG@20]
)
print("in here2")
print(result)
print("in here3")