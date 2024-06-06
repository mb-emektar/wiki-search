import pyterrier as pt
from pyterrier.measures import *

pt.init()

dataset = pt.get_dataset('irds:dpr-w100/natural-questions/dev')
index_ref = pt.IndexRef.of('./indices/dpr-w100')
pipeline = pt.BatchRetrieve(index_ref, wmodel='BM25')
bm25_qe = pt.BatchRetrieve(index_ref, wmodel="BM25", controls={"qe" : "on"})

# (optionally other pipeline components)

print("in here1")
result = pt.Experiment(
    [pipeline],
    dataset.get_topics('text'),
    dataset.get_qrels(),
    [MAP, nDCG@20]
)
print("Result:")
print(result)
print("in here3")

print("------------------------")
print("------------------------")

print("in here4")
result2 = pt.Experiment(
    [bm25_qe],
    dataset.get_topics('text'),
    dataset.get_qrels(),
    [MAP, nDCG@20]
)
print("Result bm25_qe:")
print(result2)
print("in here3")