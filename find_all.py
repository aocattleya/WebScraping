# ライブラリの読み込み
from bs4 import BeautifulSoup
import urllib.request

# URL
url = "https://github.com/aocattleya"

# urlにアクセス 
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで見えるように
soup = BeautifulSoup(html, "html.parser")

# 出力する
print(soup.find_all('span',class_='repo js-pinnable-item'))

# 一つ目の要素を抽出する
print(soup.find_all('span',class_='repo js-pinnable-item')[0].get_text())