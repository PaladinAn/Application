# 以Chrome為例，進行爬取
# 按F12，按network，按F5，找請求的資訊；再以pythono模擬請求
# 按Preview，查看資料
# 按Headers，可找到該請求網址
# 在Response Headers 下 的 content-type，可找到該頁面格式

import request as req
# 爬取到的資訊寫入EXCEL
from openpyxl import Workbook

#　創建excel檔案
wb = Workbook
# 創建工作表
ws = wb.active

# 我想要取得的資訊
title = ['名稱', '價格', '數量']
# 加入列表
ws.append(title)

# 避免，防爬蟲機制，被擋掉，修改ueser-agent，貼上ueser-agent資訊
header ={
  'ueser-agent': ''
}

# 設定範圍頁數
for index in range(28):
# 輸入網址
  url = ''
  # 因為網只要一直變動
  url = url + str(index)
  # 印出來可知道印到第幾頁
  print(url)
  # 發送請求
  r = req.get(url, headers=header)
  # 印出回應
  print(r)
  # 字典解析，假設對方網頁格式，是json
  root_json = r.json
  
  # 利用for迴圈，爬資訊
  for data in root_json['data']:
    course = []
    # 第一個要取得資訊的位置: data底下的title
    course.append(data['title'])
    # 第二個要取得資訊的位置: data底下的owner的price
    course.append(data['owner']['price'])
    # 第二個要取得資訊的位置: 
    course.append(data['owner']['quantity'])
    
    # 列表寫入Excel
    ws.append(course)
# 存檔
wb.save('data.xlsx')
