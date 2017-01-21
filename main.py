import urllib2
import os
import errno

def generateURLs():
    urls = []
    start = 1
    end = 20
    runner = 1
    while runner <= end:
        number = 100 + runner
        s = "http://atla.avatarspirit.net/transcripts.php?num=" + str(number)
        urls.append(s)
        number += 100
        s = "http://atla.avatarspirit.net/transcripts.php?num=" + str(number)
        urls.append(s)
        number += 100
        s = "http://atla.avatarspirit.net/transcripts.php?num=" + str(number)
        urls.append(s)
        runner += 1
    s = "http://atla.avatarspirit.net/transcripts.php?num=321"
    urls.append(s)
    print urls
    return urls

def openPages(pages):
    for p in pages:
        f = urllib2.urlopen(p)
        f = f.read()
        title = "s"+str(p[49]) + "e"+str(p[50:52])+".html"
        writeHtmlToFile(f, title)

def writeHtmlToFile(html, title):

    start = html.index("<blockquote>") + 12;
    end = html.index("</blockquote>")
    filename = "./scripts/"
    if not os.path.exists(filename):
        os.makedirs(filename)
    f = open(filename+title, "w")
    f.write(html[start:end])
    print("Complete " + filename+title)

pages = generateURLs()
openPages(pages)