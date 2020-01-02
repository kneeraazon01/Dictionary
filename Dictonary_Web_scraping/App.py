import sys
import requests
from bs4 import BeautifulSoup as bs
import difflib

url = "https://www.dictionary.com/browse/"

try:
    word = sys.argv[1]
    url += word
except:
    print("Please Type a word")
    exit(-1)


try:
    r = requests.get(url)
    soup = bs(r.content, "lxml")
except:
    print("You're probably not connected to the internet!")
    exit(-1)


try:
    header = soup.findAll("span", {"class": "luna-pos"})[0].text
    answer_list = soup.findAll("ol")[0]
    meanings = answer_list.findChildren("li", recursive=False)
except:
    print("Word not found!")
    exit(-1)


print()
print(word + ": " + header)

for (i, meaning) in enumerate(meanings):
    print()
    print(str(i + 1) + ".", meaning.text)
