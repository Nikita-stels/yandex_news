import requests
from bs4 import BeautifulSoup as bs

header = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_11_6) AppleWebKit / 537.36"
          }

base_url = "https://news.yandex.ru/yandsearch?text=нововсти&rpt=nnews2&grhow=clutop"

def parser(header, base_url):
    ssesion = requests.Session()
    request = ssesion.get(base_url, headers=header)
    if request.status_code == 200:
        soup = bs(request.content, "html.parser")
        print(soup)

parser(header, base_url)