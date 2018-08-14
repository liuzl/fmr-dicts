#!/usr/bin/python
import lxml
import lxml.html
import lxml.etree
import urllib2
url = 'http://zh.wikipedia.org/zh-cn/%E4%B8%96%E7%95%8C%E4%B8%8A%E7%9A%84%E5%9B%BD%E5%AE%B6'
content = urllib2.urlopen(url).read().decode('utf-8','ignore')
doc = lxml.html.document_fromstring(content)
tables = doc.xpath('//table[@width="90%"]')
for table in tables:
    for tr in table.xpath('tr')[1:]:
        n1 = tr.xpath('td[1]//a/@title')[0]
        n2 = tr.xpath('td[2]/text()')[0]
        n3 = tr.xpath('td[3]/text()')[0]
        line = "%s\t%s\t%s" % (n1, n2, n3)
        print line.encode('utf-8')
