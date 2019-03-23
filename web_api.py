# ライブラリの読み込み
import json
import urllib.request

# URL
url = 'https://api.openbd.jp/v1/get?isbn=4873115655'
# URLにアクセス
response = urllib.request.urlopen(url)
# JSONデータをcontentに代入
content = json.loads(response.read().decode('utf8'))
# 欲しいデータを指定
text = content[0]['onix']['CollateralDetail']['TextContent'][0]['Text']
# 出力
print(text)