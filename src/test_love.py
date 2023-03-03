## import lib
import pandas as pd

## 讀取需要的資料(excel)

usecols = ['大限/流年','天干','地支','大限宮位', '本命宮位', # '天干' = 1,'地支' =2 '大限宮位' = 3, '本命宮位' = 4
'主星1','主星1本命四化','主星1大限四化','主星1流年四化', #'主星1'=5,'主星1本命四化'=6,'主星1大限四化'=7,'主星1流年四化'=8
'主星2','主星2本命四化','主星2大限四化','主星2流年四化', #'主星2'=9,'主星2本命四化'=10,'主星2大限四化'=11,'主星2流年四化'=12
'本命祿存','大限祿存','流年祿存',   #'本命祿存' = 13 ,'大限祿存' = 14 ,'流年祿存' = 15 
'本命擎羊','大限擎羊','流年擎羊',   #'本命擎羊' = 16 ,'大限擎羊' = 17 ,'流年擎羊' = 18 
'本命陀羅','大限陀羅','流年陀羅',   #'本命陀羅' = 19 ,'大限陀羅' = 20 ,'流年陀羅' = 21
'火星','鈴星','地空','地劫', #'火星' = 22 ,'鈴星' =23 ,'地空' =24 ,'地劫' =25 
'本命紅鸞','流年紅鸞',   #'本命紅鸞' = 26 ,'流年紅鸞' = 27
'本命天喜','流年天喜',   #'本命天喜' = 28 ,'流年天喜' = 29
'文昌','文昌本命四化','文昌大限四化','文昌流年四化', # '文昌' = 30 ,'文昌本命四化' = 31 ,'文昌大限四化' = 32 ,'文昌流年四化' = 33
'文曲','文曲本命四化','文曲大限四化','文曲流年四化', # '文曲' = 34 ,'文曲本命四化' = 35 ,'文曲大限四化' = 36 ,'文曲流年四化' = 37
'左輔','左輔本命四化','左輔大限四化','左輔流年四化', # '左輔' = 38 ,'左輔本命四化' = 39 ,'左輔大限四化' = 40 ,'左輔流年四化' = 41
'右弼','右弼本命四化','右弼大限四化','右弼流年四化', # '右弼' = 42 ,'右弼本命四化' = 43 ,'右弼大限四化' = 44 ,'右弼流年四化' = 45
'boshi'] # 'boshi' = 46

GanToGi ={ '甲':'太陽','乙':'太陰','丙':'廉貞','丁':'巨門','戊':'天機',
          '己':'文曲','庚':'天相','辛':'文昌','壬':'武曲','癸':'貪狼',
    }

love_star = ['貪狼','天同','太陰','巨門','破軍','文曲','天相']

source = pd.read_csv("/Users/essen/LocalData/NCTU/Fate/data/test/Husan-1996-7-10-15-30.csv", encoding= 'big5', usecols=usecols)


## 讀取需要的欄位
## 本命 data.iloc[0:11] 1限[12:23] 2限[144:155] n限 [12+132(n-1):23+132(n-1)]
# print(data.iloc[0:11])
# print(data.iloc[12:23])

n=2
shen = source.iloc[12+132*(n-1):23+132*(n-1)]

##運限夫妻宮干飛化忌入大命
## "大限宮位 (大夫)的天干，如天干為甲(見備註)，太陽化忌，檢查大命命宮內是否有太陽星。

def Rule1(shen):
    ## Check ['大限宮位'] == '大夫' 的index為何
    bigfu_id = shen.index[shen['大限宮位'] == '大夫'].to_list()
    ## 大限宮位 (大夫)的天干，如天干為甲
    ## 太陽化忌
    Gi = GanToGi[shen['天干'][bigfu_id].to_list()[0]]
    ## 檢查大命命宮內是否有太陽星。

    ## Check ['大限宮位'] == '大夫' 的index為何
    bigmin_id = shen.index[shen['大限宮位'] == '大命'].to_list()

    star_list =[] 
    star_list += shen['主星1'][bigmin_id].to_list()
    star_list += shen['主星2'][bigmin_id].to_list()

    ##檢查大命命宮內是否有太陽星。
    if Gi in star_list:
        return 1
    else:
        return 0
    
def Rule2(shen):
    ## Check ['大限宮位'] == '大夫' 的index為何
    bigfu_id = shen.index[shen['大限宮位'] == '大夫'].to_list()
    ## 大限宮位 (大夫)的天干，如天干為甲
    ## 太陽化忌
    Gi = GanToGi[shen['天干'][bigfu_id].to_list()[0]]
    ## 檢查大命命宮內是否有太陽星。

    ## Check ['大限宮位'] == '大夫' 的index為何
    bigmin_id = shen.index[shen['本命宮位'] == '本命'].to_list()

    star_list =[] 
    star_list += shen['主星1'][bigmin_id].to_list()
    star_list += shen['主星2'][bigmin_id].to_list()

    ##檢查大命命宮內是否有太陽星。
    return 1 if Gi in star_list else 0

##"大限宮位 (大子)的天干，如天干為甲(見備註)，太陽化忌，非桃花星，邏輯結束
##大限宮位 (大子)的天干，如天干為乙(見備註)，太陰化忌，桃花星，檢查大命命宮內是否有太陰星
def Rule3(shen,start,end):
    ## Check ['大限宮位'] == '大子' 的index為何
    bigzhi_id = shen.index[shen['大限宮位'] == '大子'].to_list()

    ## 對拱位置
    mid = (int((start+end)/2)+1)
    bigzhi_id_6 = int(bigzhi_id[0])+6 if int(bigzhi_id[0]) < mid else int(bigzhi_id[0])-6
    mid_star_1 = shen['主星1'][bigzhi_id_6]
    mid_star_2 = shen['主星2'][bigzhi_id_6]

    ## 大限宮位 (大夫)的天干，如天干為甲
    ## 太陽化忌
    Gi = GanToGi[shen['天干'][bigzhi_id].to_list()[0]]
    ## 檢查大命命宮內是否有太陽星。
    bigmin_id = shen.index[shen['大限宮位'] == '大命'].to_list()

    star_list =[] 
    star_list += shen['主星1'][bigmin_id].to_list()
    star_list += shen['主星2'][bigmin_id].to_list()

    if Gi in love_star:
        ##檢查大命命宮內是否有太陰星。
        return 1 if Gi in star_list else 0
    elif Gi == '廉貞' and (mid_star_1 in love_star or mid_star_2 in love_star) :
        return 1 if Gi in star_list else 0
    elif Gi == '廉貪' and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    elif Gi == '廉相' and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    elif Gi == '廉破'and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    else:
        return 0

def Rule4(shen,start,end):
    ## Check ['大限宮位'] == '大子' 的index為何
    bigzhi_id = shen.index[shen['大限宮位'] == '大子'].to_list()

    ## 對拱位置
    mid = (int((start+end)/2)+1)
    bigzhi_id_6 = int(bigzhi_id[0])+6 if int(bigzhi_id[0]) < mid else int(bigzhi_id[0])-6
    mid_star_1 = shen['主星1'][bigzhi_id_6]
    mid_star_2 = shen['主星2'][bigzhi_id_6]

    ## 大限宮位 (大夫)的天干，如天干為甲
    ## 太陽化忌
    Gi = GanToGi[shen['天干'][bigzhi_id].to_list()[0]]
    ## 檢查本命命宮內是否有太陽星。
    bigmin_id = shen.index[shen['本命宮位'] == '命宮'].to_list()

    star_list =[] 
    star_list += shen['主星1'][bigmin_id].to_list()
    star_list += shen['主星2'][bigmin_id].to_list()

    if Gi in love_star:
        ##檢查大命命宮內是否有太陰星。
        return 1 if Gi in star_list else 0
    elif Gi == '廉貞' and (mid_star_1 in love_star or mid_star_2 in love_star) :
        return 1 if Gi in star_list else 0
    elif Gi == '廉貪' and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    elif Gi == '廉相' and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    elif Gi == '廉破'and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    else:
        return 0

def Rule5(shen,start,end):
    ## Check ['大限宮位'] == '大子' 的index為何
    bigzhi_id = shen.index[shen['大限宮位'] == '大田'].to_list()

    ## 對拱位置
    mid = (int((start+end)/2)+1)
    bigzhi_id_6 = int(bigzhi_id[0])+6 if int(bigzhi_id[0]) < mid else int(bigzhi_id[0])-6
    mid_star_1 = shen['主星1'][bigzhi_id_6]
    mid_star_2 = shen['主星2'][bigzhi_id_6]

    ## 大限宮位 (大夫)的天干，如天干為甲
    ## 太陽化忌
    Gi = GanToGi[shen['天干'][bigzhi_id].to_list()[0]]
    ## 檢查大命命宮內是否有太陽星。
    bigmin_id = shen.index[shen['大限宮位'] == '大命'].to_list()

    star_list =[] 
    star_list += shen['主星1'][bigmin_id].to_list()
    star_list += shen['主星2'][bigmin_id].to_list()

    if Gi in love_star:
        ##檢查大命命宮內是否有太陰星。
        return 1 if Gi in star_list else 0
    elif Gi == '廉貞' and (mid_star_1 in love_star or mid_star_2 in love_star) :
        return 1 if Gi in star_list else 0
    elif Gi == '廉貪' and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    elif Gi == '廉相' and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    elif Gi == '廉破'and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    else:
        return 0
    
def Rule6(shen,start,end):
    ## Check ['大限宮位'] == '大子' 的index為何
    bigzhi_id = shen.index[shen['大限宮位'] == '大田'].to_list()

    ## 對拱位置
    mid = (int((start+end)/2)+1)
    bigzhi_id_6 = int(bigzhi_id[0])+6 if int(bigzhi_id[0]) < mid else int(bigzhi_id[0])-6
    mid_star_1 = shen['主星1'][bigzhi_id_6]
    mid_star_2 = shen['主星2'][bigzhi_id_6]

    ## 大限宮位 (大夫)的天干，如天干為甲
    ## 太陽化忌
    Gi = GanToGi[shen['天干'][bigzhi_id].to_list()[0]]
    ## 檢查本命命宮內是否有太陽星。
    bigmin_id = shen.index[shen['本命宮位'] == '命宮'].to_list()

    star_list =[] 
    star_list += shen['主星1'][bigmin_id].to_list()
    star_list += shen['主星2'][bigmin_id].to_list()

    if Gi in love_star:
        ##檢查大命命宮內是否有太陰星。
        return 1 if Gi in star_list else 0
    elif Gi == '廉貞' and (mid_star_1 in love_star or mid_star_2 in love_star) :
        return 1 if Gi in star_list else 0
    elif Gi == '廉貪' and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    elif Gi == '廉相' and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    elif Gi == '廉破'and shen['主星2'][bigzhi_id] in love_star:
        return 1 if Gi in star_list else 0
    else:
        return 0

def Rule7(shen):
    ## Check ['大限宮位'] == '大夫' 的index為何
    bigfu_id = shen.index[shen['大限宮位'] == '大命'].to_list()
    ## 大限宮位 (大夫)的天干，如天干為甲
    ## 太陽化忌
    Gi = GanToGi[shen['天干'][bigfu_id].to_list()[0]]
    ## 檢查大命命宮內是否有太陽星。

    ## Check ['大限宮位'] == '大夫' 的index為何
    bigmin_id = shen.index[shen['大限宮位'] == '大夫'].to_list()

    star_list =[] 
    star_list += shen['主星1'][bigmin_id].to_list()
    star_list += shen['主星2'][bigmin_id].to_list()

    ##檢查大命命宮內是否有太陽星。
    if Gi in star_list:
        return 1
    else:
        return 0
    
def Rule8(shen):
    ## Check ['大限宮位'] == '大夫' 的index為何
    bigfu_id = shen.index[shen['大限宮位'] == '大命'].to_list()
    ## 大限宮位 (大夫)的天干，如天干為甲
    ## 太陽化忌
    Gi = GanToGi[shen['天干'][bigfu_id].to_list()[0]]
    ## 檢查大命命宮內是否有太陽星。

    ## Check ['大限宮位'] == '大夫' 的index為何
    bigmin_id = shen.index[shen['本命宮位'] == '命宮'].to_list()

    star_list =[] 
    star_list += shen['主星1'][bigmin_id].to_list()
    star_list += shen['主星2'][bigmin_id].to_list()

    ##檢查大命命宮內是否有太陽星。
    if Gi in star_list:
        return 1
    else:
        return 0

def Rule9(shen):
    ## Check ['大限宮位'] == '大夫' 的index為何
    bigfu_id = shen.index[shen['本命宮位'] == '命宮'].to_list()
    ## 大限宮位 (大夫)的天干，如天干為甲
    ## 太陽化忌
    Gi = GanToGi[shen['天干'][bigfu_id].to_list()[0]]
    ## 檢查大命命宮內是否有太陽星。

    ## Check ['大限宮位'] == '大夫' 的index為何
    bigmin_id = shen.index[shen['大限宮位'] == '大夫'].to_list()

    star_list =[] 
    star_list += shen['主星1'][bigmin_id].to_list()
    star_list += shen['主星2'][bigmin_id].to_list()

    ##檢查大命命宮內是否有太陽星。
    if Gi in star_list:
        return 1
    else:
        return 0

def Rule10(shen):
    ## Check ['大限宮位'] == '大夫' 的index為何
    bigfu_id = shen.index[shen['大限宮位'] == '大夫'].to_list()

    star_chi_list =[] 
    star_chi_list += shen['主星1本命四化'][bigfu_id].to_list()
    star_chi_list += shen['主星1大限四化'][bigfu_id].to_list()
    star_chi_list += shen['主星1流年四化'][bigfu_id].to_list()
    star_chi_list += shen['主星2本命四化'][bigfu_id].to_list()
    star_chi_list += shen['主星2大限四化'][bigfu_id].to_list()
    star_chi_list += shen['主星2流年四化'][bigfu_id].to_list()
    # print(star_chi_list)

    if '忌' in star_chi_list:
        return 1
    else:
        return 0

def Rule11(shen):
        ## Check ['大限宮位'] == '大夫' 的index為何
    bigfu_id = shen.index[shen['大限宮位'] == '大夫'].to_list()

    star_chi_list =[] 
    star_chi_list += shen['火星'][bigfu_id].to_list()
    star_chi_list += shen['鈴星'][bigfu_id].to_list()
    star_chi_list += shen['大限擎羊'][bigfu_id].to_list()
    star_chi_list += shen['大限陀羅'][bigfu_id].to_list()
    print(star_chi_list)

    if '1' in star_chi_list:
        return 1
    else:
        return 0

print(Rule11(shen))

def Rule12(shen):

    ## Check ['大限宮位'] == '大夫' 的index為何
    bigfu_id = shen.index[shen['大限宮位'] == '大夫'].to_list()

    star_chi_list =[] 
    star_chi_list += shen['火星'][bigfu_id].to_list()
    star_chi_list += shen['鈴星'][bigfu_id].to_list()
    star_chi_list += shen['大限擎羊'][bigfu_id].to_list()
    print(star_chi_list)

    if '1' in star_chi_list:
        return 1
    else:
        return 0
    
print(Rule12(shen))