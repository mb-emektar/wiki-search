import pyterrier as pt
from pyterrier.measures import *

pt.init()

dataset = pt.get_dataset('irds:dpr-w100/natural-questions/dev')
index_ref = pt.IndexRef.of('./indices/dpr-w100-nonstem') # change the path if doesnt work
pipeline = pt.BatchRetrieve(index_ref, wmodel='BM25')
# (optionally other pipeline components)

print("in here1")
result = pt.Experiment(
    [pipeline],
    dataset.get_topics('text'),
    dataset.get_qrels(),
    [MAP, nDCG@20]
)
print("Result non modified:")
print(result)
print("in here3")