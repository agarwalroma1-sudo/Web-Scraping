import pandas as pd
import requests
from io import StringIO

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

headers = {
    "User-Agent" : "Mozilla/5.0"
}

response = requests.get(url, headers = headers)

#print(response)

content = StringIO(response.text)

tables = pd.read_html(content)
print(tables)
print(len(tables))

import pandas as pd
#pd.to_csv(tables)
print(type(tables[0]))
df = pd.DataFrame(tables[0])

#print(df)
df.to_csv("countries.csv")
print("file has been created")

