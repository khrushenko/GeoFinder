# -*- coding: utf-8 -*-
__author__ = 'master'

import unittest
import func


class TestURL(unittest.TestCase):
    def test_getLinks(self):
        links = func.getLinks("rss.xml", "rss")
        self.assertNotEqual(links, [])
        links = func.getLinks("rss.xml", "invalid")
        self.assertEqual(links, [])
        links = func.getLinks("", "")
        self.assertEqual(links, [])

    def test_isLastDay(self):
        day = func.isLastDay("Sat, 09 May 2015 17:41:42 +0300")
        self.assertEqual(day, True)
        day = func.isLastDay("Sat, 08 May 2015 17:41:42 +0300")
        self.assertEqual(day, False)

    def test_transliterate(self):
        str = func.transliterate(u'Київ')
        self.assertEqual(str, "Kyiv")
        str = func.transliterate("")
        self.assertEqual(str, "")

    def test_openURL(self):
        rss = []
        func.openURL("http://tsn.ua/rss", rss)
        self.assertNotEqual(rss, [])
        rss = []
        func.openURL("", rss)
        self.assertEqual(rss, ['Error URL'])

    def test_writeCityToXml(self):
        list = {'Kyiv': 1}
        testFile = 'Tests/test.xml'
        func.writeCityToXml(open(testFile, "wt"), list)
        self.assertEqual(open(testFile, 'r').read(),
                         '<?xml version="1.0" ?><CityList><city>'
                         '<name>Kyiv</name><count>1</count></city></CityList>')

    def test_findGeo(self):
        results = {}
        func.findGeo([], [], results)
        self.assertEqual(results, {})
