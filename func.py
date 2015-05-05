# -*- coding: utf-8 -*-

import urllib2, time, email.utils
from xml.dom.minidom import *

# Відкриває XML-файл і повертає список текстових значень.
def getLinks(filename, tag):
    try:
        xml = parse(filename)
    except:
        return []
    nodeSet = xml.getElementsByTagName(tag)
    ret = []
    for url in nodeSet:
        ret.append(url.childNodes[0].nodeValue)
    return ret

# Відкриває отриману URL і повертає її вміст.
def openURL(url):
    try:
        temp = urllib2.urlopen(url)
        html = temp.read()
        temp.close()
    except:
        html = "Error url"
    return html

# Записує у файл в форматі XML вміст списку.
def writeCityToXml(file, list):
    impl = getDOMImplementation()
    doc = impl.createDocument(None, "RSSList", None)
    top = doc.documentElement
    top.tagName = "CityList"
    for city in list:
        elements = doc.createElement("city")
        top.appendChild(elements)
        element = doc.createElement("name")
        element.appendChild(doc.createTextNode(city))
        elements.appendChild(element)
        element = doc.createElement("count")
        element.appendChild(doc.createTextNode(str(list[city])))
        elements.appendChild(element)
        top.appendChild(elements)
    doc.writexml(file)

def isLastDay(checkedTime):
    return time.time() - time.mktime(email.utils.parsedate(checkedTime)) <= 24 * 3600

def transliterate(string):

    capital_letters = {u'А': u'A',
                       u'Б': u'B',
                       u'В': u'V',
                       u'Г': u'G',
                       u'Д': u'D',
                       u'Е': u'E',
                       u'Є': u'E',
                       u'Ж': u'Zh',
                       u'З': u'Z',
                       u'И': u'Y',
                       u'І': u'I',
                       u'Ї': u'I',
                       u'Й': u'Y',
                       u'К': u'K',
                       u'Л': u'L',
                       u'М': u'M',
                       u'Н': u'N',
                       u'О': u'O',
                       u'П': u'P',
                       u'Р': u'R',
                       u'С': u'S',
                       u'Т': u'T',
                       u'У': u'U',
                       u'Ф': u'F',
                       u'Х': u'H',
                       u'Ц': u'Ts',
                       u'Ч': u'Ch',
                       u'Ш': u'Sh',
                       u'Щ': u'Sch',
                       u'Ь': u'',
                       u'Ю': u'Yu',
                       u'Я': u'Ya',}

    lower_case_letters = {u'а': u'a',
                       u'б': u'b',
                       u'в': u'v',
                       u'г': u'g',
                       u'д': u'd',
                       u'е': u'e',
                       u'є': u'e',
                       u'ж': u'zh',
                       u'з': u'z',
                       u'и': u'y',
                       u'і': u'i',
                       u'ї': u'i',
                       u'й': u'y',
                       u'к': u'k',
                       u'л': u'l',
                       u'м': u'm',
                       u'н': u'n',
                       u'о': u'o',
                       u'п': u'p',
                       u'р': u'r',
                       u'с': u's',
                       u'т': u't',
                       u'у': u'u',
                       u'ф': u'f',
                       u'х': u'h',
                       u'ц': u'ts',
                       u'ч': u'ch',
                       u'ш': u'sh',
                       u'щ': u'sch',
                       u'ь': u'',
                       u'ю': u'yu',
                       u'я': u'ya',}

    translit_string = ""

    for index, char in enumerate(string):
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
            if len(string) > index+1:
                if string[index+1] not in lower_case_letters.keys():
                    char = char.upper()
            else:
                char = char.upper()
        translit_string += char

    return translit_string