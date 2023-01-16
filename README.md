# Fate Datebase Generation
[TOC]

## 使用步驟

### 安裝chromdriver
1. 確認現在使用chrome版本

     - 在電腦上開啟Chrome。
     - 按一下右上方的 **「更多」** 圖示 。
     - 依序按一下 **[說明]** **[關於Google Chrome]**。

> [參考連結](https://support.google.com/chrome/answer/95414?hl=zh-Hant&co=GENIE.Platform%3DDesktop)

2. 根據 **步驟1** 所顯示的chrome版本，下載對應的chromedrive放到資料夾中
    - 透過 https://chromedriver.chromium.org/downloads 下載對應版本的chromedrive
    - 放到執行程式的資料夾中 (複製路徑)
    - 將 410 行 PATH = "改成剛剛複製的路徑" 
![](https://i.imgur.com/oSC0gPh.png)


---

### 安裝Python 3.9.15

1. 透過此連結[下載 Python 3.9.15 ](https://www.python.org/downloads/release/python-3915/)
2. 先點選下方Add Python3.9 to Path
3. 再點選Install Now進行安裝
4. 靜候佳音，等待他安裝完成
5. 需要編輯器（集成開發環境,IDE）才能開始寫程式 - 我是使用 [VS code](https://code.visualstudio.com/)，可以選擇自己喜歡的～
6. 下載套件 (從terminal端打以下指令)
```
# （packgeName = selenium, bs4, calendar, time, csv, argparse)
pip3 install [packageName]
```
[參考連結：https://www.codingspace.school/blog/2021-04-07
](https://www.codingspace.school/blog/2021-04-07)

## 使用 generate_database.py 生成命盤資料庫

1. 透過 [Github](https://github.com/Essen-Lin/Fate/blob/main/generate_database.py) 下載 code 
2. 開啟Terminal（ VS code 下方即有terminal 環境）
3. 根據 受測者的 名稱/性別/出生時間 在 terminal 中 輸入對應的指令 
    * [-n] : 受測者姓名
    * [-g] : 受測者性別 （woman/w or man/m)
    * [-Y] : 出生西元年
    * [-M] : 出生月份
    * [-D] : 出生日期
    * [-o] : 出生時間（時）
    * [-m] : 出生時間（分）

4. 在data這個資料夾下可以找到對應生成的[資料庫](https://github.com/Essen-Lin/Fate/blob/main/data/Essen-1996-7-10-15-30.csv)

```

python3.9 generate_database.py [-n Name] [-g Gender] [-Y Year] [-M Month] [-D Day] [-o hour] [-m mins]

Example:
python3.9 generate_database.py -n Husan -g woman -Y 1996 -M 7 -D 10 -o 15 -m 30

```

## 將問卷資料自動輸出成命盤資料庫

1. 來自聖軒老師提供的 [命盤資料](https://)
![](https://i.imgur.com/f6X0M3Y.png)

2. 透過 剛剛的自動化生成程式 [generate_database.py](https://github.com/Essen-Lin/Fate/blob/main/generate_database.py)，輸入對應的指令
- id 對應  [-n] : 受測者姓名
- v1 對應 [-g] : 受測者性別 （woman/w or man/m)
- year 對應 [-Y] : 出生西元年
- s.mon 對應 [-M] : 出生月份
- s.day 對應 [-D] : 出生日期
- s.hour 對應 [-o] : 出生時間（時）
- s.min 對應 [-m] : 出生時間（分）



| id         |     v1     | year       | s.mon    |  s.day   | s.hour         | s.min          |
| ---------- |:----------:| ---------- | -------- |:--------:| -------------- | -------------- |
| [-n]       |    [-g]    | [-Y]       | [-M]     |   [-D]   | [-o]           | [-m]           |
| 受測者姓名 | 受測者性別 | 出生西元年 | 出生月份 | 出生日期 | 出生時間（時） | 出生時間（分） |


3. 寫成腳本程式 並且 執行程式

```
python3 run_tscs992.py
```

4. 在data這個資料夾下可以找到對應生成的[資料庫](https://github.com/Essen-Lin/Fate/blob/main/data)
* [100個測試資料](https://github.com/Essen-Lin/Fate/tree/main/data/100_tscs992)


    


---
> [name=Essen Lin]
>[time=Mon, Dec 19, 2022 4:09 PM]