import pyterrier as pt

# PyTerrier'ı başlat
pt.init()

# Önceden oluşturulmuş indexi yükle
index_ref_stem = "/Users/berkguler/Downloads/older/master/CENG 596 - Info Retrieval/project/indices/dpr-w100"

# Phrase query ile BM25 modelini yükle
BM25_phrase = pt.BatchRetrieve(index_ref_stem, wmodel="BM25")

# Phrase query çalıştır
results_phrase = BM25_phrase.transform('information retrieval')

# Sonuçları yazdır
print(results_phrase)