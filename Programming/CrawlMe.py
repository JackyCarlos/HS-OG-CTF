
import hashlib
import requests
import re


def hashFiles():
    filesToHash = crawlWebsite("http://hso-hacker.space:7789/files/")
    print(filesToHash)

    filesToHash.sort(key=getNumber)
    print(filesToHash)

    result = ""

    for i in filesToHash:
        t = i.split(" ")

        m = hashlib.sha1()
        m.update(t[1].encode())

        result += m.hexdigest()

    print(result)

    m = hashlib.sha1()
    m.update(result.encode())

    sess = requests.session()
    poster = sess.post("http://hso-hacker.space:7789/", data={"shasumall": m.hexdigest(), "submit": "Submit"})
    print(poster.text)


def getNumber(elem):
    words = elem.split(" ")
    return words[0]


def crawlWebsite(url):
    sess = requests.session()

    data = sess.get(url).text

    # regex for all possible subdirectories
    directories = re.findall(r"href=\"([a-zA-Z]+)\/?\"", data)

    # Check if .hashme file exists ...
    if not directories:
        hashme = sess.get(url + "/.hashme").text

        # when the data starts with a number, congrats you found a ".hashme"-file ...
        if re.match(r"[0-9]{3}", hashme):
            print(hashme)

            return [hashme]
        pass

    resultString = []

    for direc in directories:
        nextDirectory = crawlWebsite(url + "/" + direc)

        resultString.extend(nextDirectory)

    return resultString


if __name__ == '__main__':
    hashFiles()
