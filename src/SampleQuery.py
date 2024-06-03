import pyterrier as pt
from QueryTransform import QueryTransform


# PyTerrier'ı başlat
pt.init()

# Önceden oluşturulmuş indexi yükle
index_ref_stem = './indices/dpr-w100'
index_ref_nonstem = './indices/dpr-w100-nonstem'


# BM25 modelini yükle ve stemming'i etkinleştir
BM25_stem = pt.BatchRetrieve(index_ref_stem, wmodel="BM25")

# BM25 modelini yükle
BM25_nonstem = pt.BatchRetrieve(index_ref_nonstem, wmodel="BM25")


# Sorguyu tanımla
query = "Turkey is a predominantly mountainous country, and true lowland is confined to the coastal fringes."
#queryTransformer = QueryTransform()
#transformedQuery = queryTransformer.process_text(query)

# Sorguyu çalıştır ve sonuçları al
results_stem = BM25_stem.transform(query)
#results_stem_transform = BM25_stem.transform(transformedQuery)
results_unstem = BM25_nonstem.transform(query)

# Sonuçları yazdır
print(results_stem)
print("------------------------")
print("------------------------")
print("------------------------")
print(results_unstem)
#print(results_unstem)
