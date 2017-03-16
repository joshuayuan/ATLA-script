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
    urls.sort()
    print urls
    return urls

def openPages(pages):
    count = 0
    for p in pages:
        f = urllib2.urlopen(p)
        f = f.read()
        title = "s"+str(p[49]) + "e"+str(p[50:52])
        writeHtmlToFile(f, title, count)
        count+=1

def writeHtmlToFile(html, title, count):

    start = html.index("<blockquote>") + 12;
    end = html.index("</blockquote>")
    filename = "./scripts/"
    if not os.path.exists(filename):
        os.makedirs(filename)
    f = open(filename+title+".html", "w")
    yaml = "---\n    layout: scripts\n    title: " + str(title) + "\n    order: "+str(count) +"\n---\n"
    header = "<h1> " + title + "</h1>\n"
    ts = html[start:end]
    f.write(yaml + header + ts)
    print("Complete " + filename+title)

pages = generateURLs()
openPages(pages)
