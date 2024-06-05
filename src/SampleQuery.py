import pyterrier as pt
from QueryTransform import QueryTransform

# PyTerrier'ı başlat
pt.init()

# Önceden oluşturulmuş indexi yükle
index_ref = pt.IndexRef.of('./indices/dpr-w100-small')
index = pt.IndexFactory.of(index_ref)
#index_ref_non_modified = './indices/dpr-w100-nonstem'


# BM25 modelini yükle
bm25 = pt.BatchRetrieve(index_ref, wmodel="BM25")
bm25_qe = pt.BatchRetrieve(index_ref, wmodel="BM25", controls={"qe" : "on"})

# Non Modified BM25 modelini yükle
#bm25_non_modified = pt.BatchRetrieve(index_ref_non_modified, wmodel="BM25")


# Sorguyu tanımla
query = "Turkey is a predominantly mountainous country, and true lowland is confined to the coastal fringes."
#queryTransformer = QueryTransform()
#transformedQuery = queryTransformer.process_text(query)


# Sorguyu çalıştır ve sonuçları al
results = bm25.transform(query)
results_qe = bm25_qe.transform(query)
#results_transform = bm25.transform(transformedQuery)
#results_non_modified = bm25_non_modified.transform(query)
#results_non_modified_transform = bm25_non_modified.transform(transformedQuery)


# İlk 10 sonucu al
top_10_results = results.head(10)
top_10_results_qe = results_qe.head(10)
#top_10_results_transform = results_transform.head(10)

dataset = pt.get_dataset("irds:dpr-w100")
document_dict = {doc['docno']: doc for doc in dataset.get_corpus_iter()}

# Sonuçları yazdır
for _, row in top_10_results.iterrows():
    doc_id = row['docno']
    print(f"Doc ID: {doc_id}")
    doc = document_dict[doc_id]
    print(f"Title: {doc['title']}")
    print(f"Text: {doc['text'][:200]}\n")

print("------------------------")
print("------------------------")
print("------------------------")

# Sonuçları yazdır
for _, row in top_10_results_qe.iterrows():
    doc_id = row['docno']
    print(f"Doc ID: {doc_id}")
    doc = document_dict[doc_id]
    print(f"Title: {doc['title']}")
    print(f"Text: {doc['text'][:200]}\n")


'''
# Sonuçları yazdır
for _, row in top_10_results_transform.iterrows():
    doc_id = row['docno']
    print(f"Doc ID: {doc_id}")
    doc = document_dict[doc_id]
    print(f"Title: {doc['title']}")
    print(f"Text: {doc['text'][:200]}\n")

dataset = pt.get_dataset("irds:dpr-w100")
documentList = list(dataset.get_corpus_iter())


# Sonuçları yazdır
for _, row in top_10_results.iterrows():
    doc_id = row['docno']
    doc = documentList[int(doc_id)-1]
    print(f"Title: {doc['title']}")
    print(f"Text: {doc['text'][:200]}\n")


print(results[:10])
print("------------------------")
print("------------------------")
print("------------------------")
print(results_transform)
print("------------------------")
print("------------------------")
print("------------------------")
print(results_non_modified)
print("------------------------")
print("------------------------")
print("------------------------")
print(results_non_modified_transform)
'''




