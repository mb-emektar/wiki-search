import pyterrier as pt
from pyterrier.measures import *
from QueryTransform import QueryTransform
import pandas as pd

pt.init()
dataset = pt.get_dataset('irds:vaswani')
index_ref = pt.IndexRef.of('./indices/vaswani') # assumes you have already built an index
pipeline = pt.BatchRetrieve(index_ref, wmodel='BM25')

sdm = pt.rewrite.SequentialDependence()
bo1 = pt.rewrite.Bo1QueryExpansion(index_ref)

pipeline1 = sdm >> pipeline


# Queryleri al
topics = dataset.get_topics()
print(topics)
print(type(topics))
# Queryleri işle
text_processor = QueryTransform()  # TextProcessor sınıfını oluştur

processed_topics = pd.DataFrame([(topic[0], text_processor.process_text(topic[1])) for topic in topics], columns=['qid', 'text'])

print("---------------")

# (optionally other pipeline components)
result = pt.Experiment(
    [pipeline],
    dataset.get_topics(),
    dataset.get_qrels(),
    [MAP, nDCG@20]
)
print("dümdüz:")
print(result)
print("---------------")
result = pt.Experiment(
    [pipeline],
    processed_topics,
    dataset.get_qrels(),
    [MAP, nDCG@20]
)
print("processed query:")
print(result)
print("---------------")
result = pt.Experiment(
    [pipeline1],
    dataset.get_topics(),
    dataset.get_qrels(),
    [MAP, nDCG@20]
)
print("pipeline1:")
print(result)
print("---------------")
result = pt.Experiment(
    [pipeline1],
    processed_topics,
    dataset.get_qrels(),
    [MAP, nDCG@20]
)
print("pipeline1 ve processed query :")
print(result)
