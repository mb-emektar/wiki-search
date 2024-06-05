import pandas as pd
import gzip
import random

temp_output_path = 'shuffled_subset.tsv'
# Geçici dosyayı gz formatında sıkıştırarak yaz
with open(temp_output_path, 'rb') as f_in, gzip.open('shuffled_subset.tsv.gz', 'wb') as f_out:
    f_out.writelines(f_in)