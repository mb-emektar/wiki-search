import pyterrier as pt
from QueryTransform import QueryTransform

class PyTerrierSearch:
    def __init__(self, index_path, dataset_name):
        # PyTerrier'ı başlat
        pt.init()

        # Önceden oluşturulmuş indexi yükle
        self.index_ref = pt.IndexRef.of(index_path)
        self.index = pt.IndexFactory.of(self.index_ref)

        # BM25 modelini yükle pseduo relevance feedback ile
        self.bm25 = pt.BatchRetrieve(self.index_ref, wmodel="BM25", controls={"qe" : "on"})

        # Dataset'i al ve dokümanları bir sözlük yapısında sakla
        self.dataset = pt.get_dataset(dataset_name)
        self.document_dict = {doc['docno']: doc for doc in self.dataset.get_corpus_iter()}

        # Sonuçları saklamak için bir değişken
        self.results = None

    def search(self, query):
        # Transform the query
        queryTransformer = QueryTransform().process_text(query)

        # Sorguyu çalıştır ve sonuçları al
        self.results = self.bm25.transform(queryTransformer)
        return len(self.results)  # Sonuç sayısını döndür

    def get_page(self, page_number=1, page_size=10):
        if self.results is None:
            return []

        start = (page_number - 1) * page_size
        end = start + page_size

        # İlk top_k sonucu al
        top_results = self.results.iloc[start:end]

        # Sonuçları saklamak için bir liste oluştur
        output = []

        # Sonuçları işleyip sakla
        for _, row in top_results.iterrows():
            doc_id = row['docno']
            doc = self.document_dict.get(doc_id, {'title': 'N/A', 'text': 'N/A'})
            output.append({
                'doc_id': doc_id,
                'title': doc['title'],
                'text': doc['text'][:200]  # İlk 200 karakteri alınır
            })

        return output
