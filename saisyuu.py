import requests
from bs4 import BeautifulSoup
import sqlite3

# スクレイピングするURL
url = "https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view=a2"

# リクエストを送信してHTMLを取得
response = requests.get(url)
html_content = response.content

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(html_content, 'html.parser')