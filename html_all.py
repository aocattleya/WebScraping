# ライブラリの読み込み
from bs4 import BeautifulSoup
import urllib.request

# URL
url = "https://www.google.com/"
# urlにアクセス 
html = urllib.request.urlopen(url)
# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")
# 出力
print(soup)