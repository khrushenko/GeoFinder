# -*- coding: utf-8 -*-
from func import *
import gevent

urlsFile = "rss.xml"
urls = getLinks(urlsFile, "rss")
vocab = unicode(open('vocab.txt', 'r').read(), "utf-8").split(';')
rss = []
results = {}

print "Choose method:\n1 - Without Gevent\n2 - With Gevent"
print "Your choice:"
method = raw_input()

if method == '1':
    startTime = time.time()
    for url in urls:
        openURL(url, rss)
    findGeo(rss, vocab, results)
if method == '2':
    startTime = time.time()
    coroutine = []
    for url in urls:
        coroutine.append(gevent.spawn(openURL, url, rss))
    gevent.joinall(coroutine)
    findGeo(rss, vocab, results)

print('Time of program work is %s seconds' % (time.time() - startTime))

findGeo(rss, results, vocab)
writeCityToXml(open("out.xml", "wt"), results)

print results
