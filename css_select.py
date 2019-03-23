# ライブラリの読み込み
from bs4 import BeautifulSoup
import urllib.request

# URL
url = "https://github.com/aocattleya"

# URLにアクセス 
html = urllib.request.urlopen(url)

# HTMLをBeautifulSoupで見えるように
soup = BeautifulSoup(html, "html.parser")

# 出力する
print(soup.select(".text-small")[1].get_text())