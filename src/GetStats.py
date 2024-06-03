import pyterrier as pt

pt.init()

# Index dpr-w100
index_ref = pt.IndexRef.of('./indices/dpr-w100') # assumes you have already built an index
index = pt.IndexFactory.of(index_ref)

collection_stats = index.getCollectionStatistics()
print(collection_stats)

