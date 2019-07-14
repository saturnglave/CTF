#coding:utf-8
import pandas as pd
from pandas.io.json import json_normalize
import json

#元のjsonが入れ子なので、json_normalizeで修正
with open('incidents.json') as data_file:
    data = json.load(data_file)

df = json_normalize(data, 'tickets', record_prefix='tickets_')

print(df.head(1))
print(df.describe())

#Q1. most common src_ip
df_grouped1 = df.groupby('tickets_src_ip').nunique()
print(df_grouped1)

#Q2. How many unique destination IP addresses were targeted by the source IP address 251.165.34.242?
df_grouped2 = df.groupby(['tickets_src_ip','tickets_dst_ip']).count()
print(df_grouped2)
#print(df_grouped2[df_grouped2['tickets_src_ip'] == '251.165.34.242'])

#Q3. What is the number of unique destination ips a file is sent, on average? Needs to be correct to 2 decimal places.
df_grouped3 = df.groupby(['tickets_file_hash']).nunique()
print(df_grouped3)
# この結果を見て計算すると、1.40
