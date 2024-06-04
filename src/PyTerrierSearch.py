import pyterrier as pt
from QueryTransform import QueryTransform

class PyTerrierSearch:
    def __init__(self, index_path, dataset_name):
        # PyTerrier'ı başlat
        pt.init()

        # Önceden oluşturulmuş indexi yükle
        self.index_ref = pt.IndexRef.of(index_path)
        self.index = pt.IndexFactory.of(self.index_ref)

        # BM25 modelini yükle
        self.bm25 = pt.BatchRetrieve(self.index_ref, wmodel="BM25")

        # Dataset'i al ve dokümanları bir sözlük yapısında sakla
        self.dataset = pt.get_dataset(dataset_name)
        self.document_dict = {doc['docno']: doc for doc in self.dataset.get_corpus_iter()}

    def search(self, query, top_k=10):
        # Transform the query
        queryTransformer = QueryTransform().process_text(query)

        # Sorguyu çalıştır ve sonuçları al
        results = self.bm25.transform(queryTransformer)

        # İlk top_k sonucu al
        top_results = results.head(top_k)

        # Sonuçları saklamak için bir liste oluştur
        output = []

        # Sonuçları işleyip sakla
        for _, row in top_results.iterrows():
            doc_id = row['docno']
            doc = self.document_dict[doc_id]
            output.append({
                'doc_id': doc_id,
                'title': doc['title'],
                'text': doc['text'][:200]  # İlk 200 karakteri alınır
            })

        return output

# Sınıfı kullanarak arama yapma
if __name__ == "__main__":
    index_path = './indices/dpr-w100-small'
    dataset_name = "irds:dpr-w100"
    
    pt_search = PyTerrierSearch(index_path, dataset_name)
    query = "Turkey is a predominantly mountainous country, and true lowland is confined to the coastal fringes."
    
    results = pt_search.search(query)
    
    # Sonuçları yazdır
    for result in results:
        print(f"Doc ID: {result['doc_id']}")
        print(f"Title: {result['title']}")
        print(f"Text: {result['text']}\n")
