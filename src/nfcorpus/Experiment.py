import pyterrier as pt
from pyterrier.measures import *

pt.init()

# Dataset ve index tanımları
dataset = pt.get_dataset('irds:nfcorpus/dev')
index_ref = pt.IndexRef.of('./indices/nfcorpus')  # Mevcut bir dizini belirtin

# Pipeline tanımı
pipeline = pt.BatchRetrieve(index_ref, wmodel='BM25')
# (opsiyonel olarak diğer pipeline bileşenleri)

# Deneyin yürütülmesi ve sonuçların alınması
results = pt.Experiment(
    [pipeline],
    dataset.get_topics('title'),
    dataset.get_qrels(),
    [MAP, nDCG@20]
)

# Sonuçların yazdırılması
print(results)
