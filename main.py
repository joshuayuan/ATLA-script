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

generateURLs()