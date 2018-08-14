import requests
import lxml
import lxml.html
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_ethnic_groups_in_China_and_Taiwan"
content = requests.get(url).text
doc = lxml.html.document_fromstring(content)
data = doc.xpath("//table//a[@class='extiw']/text()")
pd.DataFrame(data[:-2]).to_csv("dict.txt", index=False, header=False)

