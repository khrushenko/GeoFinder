# -*- coding: utf-8 -*-
from func import *

# Підготовка списку посилань для обробки.
urlsFile = "rss.xml"
urls = getLinks(urlsFile, "rss")
vocab = unicode(open('vocab.txt', 'r').read(), "utf-8").split(';')
results = {}
for url in urls:
    xml = parseString(openURL(url))
    items = xml.getElementsByTagName("item")
    for item in items:
        if isLastDay(item.getElementsByTagName("pubDate")[0].childNodes[0].nodeValue):
            title = item.getElementsByTagName("title")[0].childNodes[0].nodeValue
            for city in vocab:
                # print title
                if city in title:
                    key = str(transliterate(city))
                    if key in results:
                        count = results[key]+1
                    else:
                        count = 1
                    results.update({key: count})
print results
writeCityToXml(open("out.xml", "wt"), results)