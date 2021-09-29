# 載入模組
import requests as req

# 輸入網址
url = 'https://tw.yahoo.com/'
# 取得網址
r = req.get(url)
# .text 文字形式讀取 .content 影片、圖片、pdf、二進制讀取
print(r.content)
# 進行儲存， with open('檔名', mode = '模式') as file:
with open('123.jpg', mode = 'wb') as file:
  file.write(r.content)
