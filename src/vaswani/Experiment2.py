import pyterrier as pt
from pyterrier.measures import *
from QueryTransform import QueryTransform
import pandas as pd

pt.init()

dataset = pt.get_dataset('irds:vaswani')

index_ref = pt.IndexRef.of('./indices/vaswani') # assumes you have already built an index
index_ref_non_modified = pt.IndexRef.of('./indices/vaswani-nonstem') # assumes you have already built an index

pipeline = pt.BatchRetrieve(index_ref, wmodel='BM25')
pipeline_non_modified = pt.BatchRetrieve(index_ref_non_modified, wmodel='BM25')

result = pt.Experiment(
    [pipeline],
    dataset.get_topics(),
    dataset.get_qrels(),
    [MAP, nDCG@20]
)

result_non_modified = pt.Experiment(
    [pipeline_non_modified],
    dataset.get_topics(),
    dataset.get_qrels(),
    [MAP, nDCG@20]
)


print("dümdüz:")
print(result)

print("---------------")
print("---------------")

print("non modified:")
print(result_non_modified)