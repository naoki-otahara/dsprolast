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

# データベース接続を作成
conn = sqlite3.connect('weather_data.db')

# カーソルオブジェクトを作成
cursor = conn.cursor()

# テーブルを作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather (
    date TEXT,
    pressure TEXT,
    rainfall TEXT,
    temp_avg TEXT,
    temp_high TEXT,
    temp_low TEXT,
    vapor_pressure TEXT,
    humidity TEXT
)
''')

# コミットして変更を確定
conn.commit()


# データをデータベースに挿入
for data in data_list:
    cursor.execute('''
    INSERT INTO weather (date, pressure, rainfall, temp_avg, temp_high, temp_low, vapor_pressure, humidity)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)

# コミットして変更を確定
conn.commit()

# データベース接続を閉じる
conn.close()
