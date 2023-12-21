from urllib.parse import urlparse
import pandas as pd

def parse_domain(url):
    urlfinal=urlparse(url).netloc.replace("www.", "")
    if not urlfinal:
        urlfinal =urlparse(url).path.replace("www.", "")
    print(urlfinal)
    return urlfinal.lower()

df=pd.read_csv('domains.csv')

for i in range(len(df)):
    df.loc[i,'domain']=parse_domain(df.loc[i,'URL'])

df.to_csv('domains_op.csv',index=None)