import pyterrier as pt

# PyTerrier'ı başlat
pt.init()

dataset = pt.get_dataset('irds:vaswani')

index_ref = pt.IndexRef.of('./indices/vaswani') # assumes you have already built an index

# Phrase query ile BM25 modelini yükle
BM25_phrase = pt.BatchRetrieve(index_ref, wmodel="BM25", controls={"matching": "phrase"})

# Phrase query çalıştır
results_phrase = BM25_phrase.transform('"information retrieval"')

# Sonuçları yazdır
print(results_phrase)