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

1. 透過 [Github](https://github.com/Essen-Lin/Fate) 下載 code 
2. 開啟Terminal（ VS code 下方即有terminal 環境）
3. 根據 受測者的 名稱/性別/出生時間 在 terminal 中 輸入對應的指令 
    * [-n] : 受測者姓名
    * [-g] : 受測者性別 （woman/w or man/m)
    * [-Y] : 出生西元年
    * [-M] : 出生月份
    * [-D] : 出生日期
    * [-o] : 出生時間（時）
    * [-m] : 出生時間（分）

4. 在data這個資料夾下可以找到對應生成的[資料庫](https://github.com/Essen-Lin/Fate)

```

python3.9 generate_database.py [-n Name] [-g Gender] [-Y Year] [-M Month] [-D Day] [-o hour] [-m mins]

Example:
python3.9 generate_database.py -n Husan -g woman -Y 1996 -M 7 -D 10 -o 15 -m 30

```

## 將問卷資料自動輸出成命盤資料庫

1. 來自聖軒老師提供的 [命盤資料](https://)
![](https://i.imgur.com/f6X0M3Y.png)

2. 透過 剛剛的自動化生成程式 [generate_database.py](https://github.com/Essen-Lin/Fate)，輸入對應的指令
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
* [1922個測試資料](https://github.com/Essen-Lin/Fate/tree/main/data/1922_tscs992)


    
## 透過 [debug_tscs992.py](https://github.com/Essen-Lin/Fate/tree/main/src)檢查生成的資料庫是否有缺漏

1. 使用 [debug_tscs992.py](https://github.com/Essen-Lin/Fate/tree/main/src)檢查生成的資料庫是否有缺漏
    ```
    # debug and confirm "run-tscs992.py" 是否有檔案沒跑到並且生成沒跑成功的檔案
    python3 debug_tscs992.py
    ```
2. 因為其中有 月份 出生時間有缺漏，因此 第 541, 1645, 1766筆資料，並未能成功生成。
![](https://i.imgur.com/IJcFsEd.png)

![](https://i.imgur.com/LhYy4w5.png)

3. 老師的資料集一共有1925個資料，由於3個資料有缺漏，因此總資料量為1922個。
---

##  根據生成出來的[命盤資料庫](https://github.com/Essen-Lin/Fate/blob/main/data) 寫對應的受測者婚姻狀況


1. RULE法則[解釋](https://docs.google.com/spreadsheets/d/1s-pzZcYCrdFz-3WI0hYbYR7kgQmymYiQgaiblHtjPlc/edit#gid=0)
2. 轉換程式: [test_love.py](https://github.com/Essen-Lin/Fate/blob/main/src/test_love.py)
3. 執行方式
```
python3 test_love.py
```
4. 生成[結果](https://github.com/Essen-Lin/Fate/blob/main/data/love_rule_1922_tscs.csv)

> [name=Essen Lin]
> [time=Mon, Dec 19, 2022 4:09 PM]
###### tags: `交大研究`