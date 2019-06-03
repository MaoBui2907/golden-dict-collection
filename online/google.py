import requests
import sys

"""
    @argv translate from ["en", "vi", "fr",... "auto"]
    @argv translate to ["en", "vi", "jp",...]
    @argv translate text ex: "Hello"
"""
src = sys.argv[1]
dst = sys.argv[2]
kw = sys.argv[3]

url = "http://translate.googleapis.com/translate_a/single?client=gtx&sl=" + \
    src + "&tl=" + dst + "&dt=t&ie=UTF-8&oe=UTF-8&q=" + kw

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
try:
    res = requests.get(url, headers=header)
    data = res.json()
    output = ""
    for i in data[0]:
        output += i[0]
    print(output)
except:
    print ("something was wrong")
