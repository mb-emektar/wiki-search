import pyterrier as pt
from QueryTransform import QueryTransform


# PyTerrier'ı başlat
pt.init()

# Önceden oluşturulmuş indexi yükle
index_ref_stem = "/Users/berkguler/Downloads/older/master/CENG 596 - Info Retrieval/project/indices/dpr-w100"
# index_ref_nonstem = "/Users/berkguler/Downloads/older/master/CENG 596 - Info Retrieval/project/indices/dpr-w100-nonstem"


# BM25 modelini yükle ve stemming'i etkinleştir
BM25_stem = pt.BatchRetrieve(index_ref_stem, wmodel="BM25", properties={"termpipelines" : "Stopwords,PorterStemmer"})

# BM25 modelini yükle
# BM25_nonstem = pt.BatchRetrieve(index_ref_nonstem, wmodel="BM25", properties={"termpipelines" : ""})


# Sorguyu tanımla
query = "Turkey is a predominantly mountainous country, and true lowland is confined to the coastal fringes."
queryTransformer = QueryTransform()
transformedQuery = queryTransformer.process_text(query)

# Sorguyu çalıştır ve sonuçları al
results_stem = BM25_stem.transform(query)
results_stem_transform = BM25_stem.transform(transformedQuery)
#results_unstem = BM25_nonstem.transform(query)

# Sonuçları yazdır
print(results_stem)
print("------------------------")
print("------------------------")
print("------------------------")
print(results_stem_transform)
#print(results_unstem)
