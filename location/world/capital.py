#!/usr/bin/python
import lxml
import lxml.html
import lxml.etree
import urllib2
url = 'http://zh.wikipedia.org/zh-cn/%E5%90%84%E5%9B%BD%E9%A6%96%E9%83%BD%E5%88%97%E8%A1%A8'
content = urllib2.urlopen(url).read().decode('utf-8','ignore')
doc = lxml.html.document_fromstring(content)
lis = doc.xpath('id("mw-content-text")/ul/li')
for li in lis:
    a = li.xpath('.//a/text()')
    print ('\t'.join(a)).encode('utf-8')
