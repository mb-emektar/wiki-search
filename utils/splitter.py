import pandas as pd
import gzip
import random

# Dosyayı oku
file_path = 'docs_real.tsv.gz'
df = pd.read_csv(gzip.open(file_path), delimiter='\t')
print('in here 1')
# Verileri karıştır
shuffled_df = df.sample(frac=1).reset_index(drop=True)
print('in here 2')

# İlk 300000 satırı seç
subset_df = shuffled_df.head(300000)
print('in here 3')
# Yeni dosyaya yaz
output_path = 'shuffled_subset.tsv'
subset_df.to_csv(output_path, sep='\t', index=False)
print('in here 4')