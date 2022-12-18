from calendar import month
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import csv
import argparse

def login(user, passwd): 
    email = driver.find_element(by=By.NAME,value='ion-input-0')
    password = driver.find_element(by=By.NAME,value='ion-input-1')
    email.send_keys(user)
    password.send_keys(passwd)
    #driver.implicitly_wait(2) # seconds
    # finding the button using xpath
    wait = WebDriverWait(driver,19990,0.01)
    # clicking on the button
    button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div/ion-content/ion-row/ion-col/ion-grid/ion-row[4]/ion-col/ion-button')))
    button.click()
    new_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div[1]/ion-header/ion-toolbar[2]/ion-buttons[2]")))
    new_button.click()

def usrname_gender(Name,gen):
    wait = WebDriverWait(driver,19990,0.01)

    man = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ion-overlay-4"]/div[2]/div/ion-list/ion-item[1]/div/ion-img[2]')))
    woman = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ion-overlay-4"]/div[2]/div/ion-list/ion-item[1]/div/ion-img[1]')))
    if gen == 'w'or'woman':
        woman.click()
    elif gen == 'm'or'man':
        man.click()
    name = driver.find_element_by_name('ion-input-0')
    name.send_keys(Name)

def set_birth_date(year,month,day,hours,mins):
    
    data_but_start = driver.find_element_by_xpath('//*[@id="picker-input"]')
    data_but_start.click()
    time.sleep(5)
    # write script - years
    script_y ="document.getElementsByClassName('picker-years')[0].getElementsByClassName('picker-item picker-picked')[0].setAttribute('data-value'," + year + ")"
    # generate a alert via javascript
    driver.execute_script(script_y)
    driver.find_element_by_css_selector('body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-years > div.picker-cell__control.picker-cell__control--prev').click()
    driver.find_element_by_css_selector('body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-years > div.picker-cell__control.picker-cell__control--next').click()

    # write script - months
    script_m ="document.getElementsByClassName('picker-months')[0].getElementsByClassName('picker-item picker-picked')[0].setAttribute('data-value'," + month + ")"
    # generate a alert via javascript
    driver.execute_script(script_m)
    driver.find_element_by_css_selector('body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-months > div.picker-cell__control.picker-cell__control--prev').click()
    driver.find_element_by_css_selector('body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-months > div.picker-cell__control.picker-cell__control--next').click()

     # write script - days
    script_d ="document.getElementsByClassName('picker-days')[0].getElementsByClassName('picker-item picker-picked')[0].setAttribute('data-value'," + day+ ")"
    # generate a alert via javascript
    driver.execute_script(script_d)
    driver.find_element_by_css_selector('body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-days > div.picker-cell__control.picker-cell__control--prev').click()
    driver.find_element_by_css_selector('body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-days > div.picker-cell__control.picker-cell__control--next').click()

     # write script - hours 
    script_h ="document.getElementsByClassName('picker-hours')[0].getElementsByClassName('picker-item picker-picked')[0].setAttribute('data-value'," + hours + ")"
    # generate a alert via javascript
    driver.execute_script(script_h)
    driver.find_element_by_css_selector('body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-hours > div.picker-cell__control.picker-cell__control--prev').click()
    driver.find_element_by_css_selector('body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-hours > div.picker-cell__control.picker-cell__control--next').click()

    # write script - mins
    script_n ="document.getElementsByClassName('picker-minutes')[0].getElementsByClassName('picker-item picker-picked')[0].setAttribute('data-value'," + mins + ")"
    # generate a alert via javascript
    driver.execute_script(script_n)
    driver.find_element_by_css_selector('body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-minutes > div.picker-cell__control.picker-cell__control--prev').click()
    driver.find_element_by_css_selector('body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-minutes > div.picker-cell__control.picker-cell__control--next').click()
    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ion-overlay-4"]/div[2]/div/ion-list/ion-row[1]/ion-col/ion-button').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="main"]/div[1]/ion-content/div[1]/ion-list/div[2]/ion-item/ion-label').click()
    
datas = []
#'大限/流年'=0,'干支'=1,
fieldnames = ['大限/流年','干支',
'主星1','主星1本命四化','主星1大限四化','主星1流年四化', #'主星1'=2,'主星1本命四化'=3,'主星1大限四化'=4,'主星1流年四化'=5
'主星2','主星2本命四化','主星2大限四化','主星2流年四化', #'主星2'=6,'主星2本命四化'=7,'主星2大限四化'=8,'主星2流年四化'=9
'本命祿存','大限祿存','流年祿存',   #'本命祿存' = 10 ,'大限祿存' = 11 ,'流年祿存' = 12 
'本命擎羊','大限擎羊','流年擎羊',   #'本命擎羊' = 13 ,'大限擎羊' = 14 ,'流年擎羊' = 15 
'本命陀羅','大限陀羅','流年陀羅',   #'本命陀羅' = 16 ,'大限陀羅' = 17 ,'流年陀羅' = 18
'火星','鈴星','地空','地劫', #'火星' = 19 ,'鈴星' =20 ,'地空' =21 ,'地劫' =22 
'本命紅鸞','流年紅鸞',   #'本命紅鸞' = 23 ,'流年紅鸞' = 24
'本命天喜','流年天喜',   #'本命天喜' = 25 ,'流年天喜' = 26
'文昌','文昌本命四化','文昌大限四化','文昌流年四化', # '文昌' = 27 ,'文昌本命四化' = 28 ,'文昌大限四化' = 29 ,'文昌流年四化' = 30
'文曲','文曲本命四化','文曲大限四化','文曲流年四化', # '文曲' = 31 ,'文曲本命四化' = 32 ,'文曲大限四化' = 33 ,'文曲流年四化' = 34
'左輔','左輔本命四化','左輔大限四化','左輔流年四化', # '左輔' = 35 ,'左輔本命四化' = 36 ,'左輔大限四化' = 38 ,'左輔流年四化' = 38
'右弼','右弼本命四化','右弼大限四化','右弼流年四化', # '右弼' = 39 ,'右弼本命四化' = 40 ,'右弼大限四化' = 41 ,'右弼流年四化' = 42
'大限宮位', '本命宮位', 'boshi'] # '大限宮位' = 43, '本命宮位' = 44, 'boshi' = 45
datas.append(fieldnames)

def crawl(url,decade):
    soup = BeautifulSoup(url, "html.parser")
    ganzhi = soup.find_all('td')

    for index in range(0,len(ganzhi)):
        if index != 5:
            i = ganzhi[index]
            try:         
                chart_unit_ganzhi = i.find(class_ = 'chart-unit-ganzhi')
                detail_datas = [' ']*46
                detail_datas [0] = decade
                detail_datas[1]= chart_unit_ganzhi.text
            except:
                pass
            
            try:
                north_star_unit = i.find(class_ = 'north-star-unit')
                detail_datas[2]= north_star_unit.text[:2]
            except:
                pass

            try:
                natal_morph = i.select_one('div.north-star-unit > span.natal-morph')
                detail_datas[3]= natal_morph.text
            except:
                pass

            try:
                decade_morph = i.select_one('div.north-star-unit > span.decade-morph')
                detail_datas[4]= decade_morph.text
            except:
                pass

            try:
                taisui_morph = i.select_one('div.north-star-unit > span.taisui-morph')
                detail_datas[5]= taisui_morph.text
            except:
                pass

            try:
                south_star_unit = i.find(class_ = 'south-star-unit')
                if (detail_datas[2]==' '):
                    detail_datas[2] = south_star_unit.text[:2]
                else:
                    detail_datas[6] = south_star_unit.text[:2]
            except:
                pass

            try:
                s_natal_morph = i.select_one('div.south-star-unit > span.natal-morph')
                if (detail_datas[6]== ' '):
                    detail_datas[3]= s_natal_morph.text
                else:
                    detail_datas[7]= s_natal_morph.text
            except:
                pass

            try:
                s_decade_morph = i.select_one('div.south-star-unit > span.decade-morph')
                if (detail_datas[6]==' '):
                    detail_datas[4]= s_decade_morph.text
                else:
                    detail_datas[8]= s_decade_morph.text
            except:
                pass

            try:
                s_taisui_morph = i.select_one('div.south-star-unit > span.taisui-morph')
                if (detail_datas[6]==' '):
                    detail_datas[5]= s_taisui_morph.text
                else:
                    detail_datas[9]= s_taisui_morph.text
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('祿存')+1):
                    detail_datas[10] = 1
                if(suppot_star_text.find('擎羊')+1):
                    detail_datas[13] = 1  
                if(suppot_star_text.find('陀羅')+1):
                    detail_datas[16] = 1
                if(suppot_star_text.find('紅鸞')+1):
                    detail_datas[19] = 1    
            except:
                pass
            
            try:
                decade_sup_star_unit_text = str(i.find(class_ = 'decade-sup-star-unit'))
                if(decade_sup_star_unit_text.find('限祿')+1):
                    detail_datas[11] = 1
                if(decade_sup_star_unit_text.find('限羊')+1):
                    detail_datas[14] = 1
                if(decade_sup_star_unit_text.find('限陀')+1):
                    detail_datas[17] = 1
            except:
                pass

            try:
                taisui_sup_star_unit_text = str(i.find(class_ = 'taisui-sup-star-unit'))
                if(taisui_sup_star_unit_text.find('年祿')+1):
                    detail_datas[12] = 1
                if(taisui_sup_star_unit_text.find('年羊')+1):
                    detail_datas[15] = 1
                if(taisui_sup_star_unit_text.find('年陀')+1):
                    detail_datas[18] = 1
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('火星')+1):
                    detail_datas[19] = 1
                if(suppot_star_text.find('鈴星')+1):
                    detail_datas[20] = 1
            except:
                pass

            try:
                suppot_star_text = str(i.find_all(class_ = 'support-star-unit'))
                if(suppot_star_text.find('地空')+1):
                    detail_datas[21] = 1
                if(suppot_star_text.find('地劫')+1):
                    detail_datas[22] = 1
            except:
                pass

            try:
                suppot_star_text = str(i.find_all(class_ = 'extra-star-unit'))
                if(suppot_star_text.find('紅鸞')+1):
                    detail_datas[23] = 1
            except:
                pass


            try:
                taisui_sup_star_unit_text = str(i.find(class_ = 'taisui-sup-star-unit'))
                if(taisui_sup_star_unit_text.find('年鸞')+1):
                    detail_datas[24] = 1
            except:
                pass

            try:
                suppot_star_text = str(i.find_all(class_ = 'extra-star-unit'))
                if(suppot_star_text.find('天喜')+1):
                    detail_datas[25] = 1
            except:
                pass


            try:
                taisui_sup_star_unit_text = str(i.find(class_ = 'taisui-sup-star-unit'))
                if(taisui_sup_star_unit_text.find('年喜')+1):
                    detail_datas[26] = 1
            except:
                pass


            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('文昌')+1):
                    detail_datas[27] = 1
                    natal_morph = i.select_one('div.support-star-unit > span.natal-morph')
                    detail_datas[28]= natal_morph.text
                    decade_morph = i.select_one('div.support-star-unit > span.decade-morph')
                    detail_datas[29]= decade_morph.text
                    taisui_morph = i.select_one('div.support-star-unit > span.taisui-morph')
                    detail_datas[30]= taisui_morph.text
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('文曲')+1):
                    detail_datas[31] = 1
                    natal_morph = i.select_one('div.support-star-unit > span.natal-morph')
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('文曲')+1):
                    natal_morph = i.select_one('div.support-star-unit > span.natal-morph')
                    detail_datas[32]= natal_morph.text
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('文曲')+1):
                    decade_morph = i.select_one('div.support-star-unit > span.decade-morph')
                    detail_datas[33]= decade_morph.text
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('文曲')+1):
                    taisui_morph = i.select_one('div.support-star-unit > span.taisui-morph')
                    detail_datas[34]= taisui_morph.text
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('左輔')+1):
                    detail_datas[35] = 1
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('左輔')+1):
                    natal_morph = i.select_one('div.support-star-unit > span.natal-morph')
                    detail_datas[36]= natal_morph.text
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('左輔')+1):
                    decade_morph = i.select_one('div.support-star-unit > span.decade-morph')
                    detail_datas[37]= decade_morph.text
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('左輔')+1):
                    taisui_morph = i.select_one('div.support-star-unit > span.taisui-morph')
                    detail_datas[38]= taisui_morph.text
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('右弼')+1):
                    detail_datas[39] = 1
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('右弼')+1):
                    natal_morph = i.select_one('div.support-star-unit > span.natal-morph')
                    detail_datas[40]= natal_morph.text
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('右弼')+1):
                    decade_morph = i.select_one('div.support-star-unit > span.decade-morph')
                    detail_datas[41]= decade_morph.text
            except:
                pass

            try:
                suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
                if(suppot_star_text.find('右弼')+1):
                    taisui_morph = i.select_one('div.support-star-unit > span.taisui-morph')
                    detail_datas[42]= taisui_morph.text
            except:
                pass

            try:
                chart_unit_decade_palace = i.find(class_ = 'chart-unit-decade-palace')
                detail_datas[43] = chart_unit_decade_palace.text
            except:
                pass

            try:
                chart_unit_natal_palace = i.find(class_ ='chart-unit-natal-palace')
                detail_datas[44]= chart_unit_natal_palace.text
            except:
                pass

            try:
                chart_unit_boshi = i.find(class_ = 'chart-unit-boshi')
                detail_datas[45]=chart_unit_boshi.text
            except:
                pass

            datas.append(detail_datas)

def write_to_csv(filename):
    crawl(driver.page_source,'本命')
    for i in range(1,11):
        shen_xpath = '//*[@id="root"]/ion-app/div[2]/ion-footer/div/div[1]/div['+str(i)+']'
        shen_source = str(i)+'限'    
        driver.find_element_by_xpath(shen_xpath).click()
        crawl(driver.page_source,shen_source)

        for i in range(1,11):
            year_xpath = '//*[@id="root"]/ion-app/div[2]/ion-footer/div/div[2]/div['+str(i)+']/span[1]'
            year_source = driver.find_element_by_xpath(year_xpath).text
            driver.find_element_by_xpath(year_xpath).click()
            crawl(driver.page_source,year_source)

    with open(filename, 'w', newline='',encoding='big5') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(datas)


	
if __name__ == "__main__":
    # Initialize  parser (Chrome) - Download the version of used chrome in the same path, and change the PATH
    PATH = "/Users/essen/Desktop/Fate/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get("https://ziweigonglue1013.firebaseapp.com/login")
    #輸入帳號密碼 - 自動登入
    login("shenglin@nctu.edu.tw","Sheng2lab")

    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-n", "--Name", help = "Input User Name", type= str)
    parser.add_argument("-g", "--Gender", help = "Input woman = w/ man = 'm", type= str)
    parser.add_argument("-Y", "--Year", help = "Birth Day (year)", type= str)
    parser.add_argument("-M", "--Month", help = "Birth Day (month)", type= int)
    parser.add_argument("-D", "--Day", help = "Birth Day (day)", type= str)
    parser.add_argument("-o", "--hour", help = "Birth time(hour)", type= str)
    parser.add_argument("-m", "--mins", help = "Birth time(mins)", type= str)
    # Read arguments from command line
    argv = parser.parse_args()

    #判斷性別(w/m) 以及輸入名稱
    # Name = 'Essen'
    # Gender = 'w'
    usrname_gender(argv.Name,argv.Gender)

    #輸入想查詢的生日
    # year = '1996'
    # input_month = 7
    # month = str(input_month-1)
    # day = '10'
    # hour = '15'
    # min = '30'

    month = str(argv.Month-1)
    set_birth_date(argv.Year,month,argv.Day,argv.hour,argv.mins) 

    time.sleep(2)
    write_to_csv(argv.Name+'-'+(argv.Year+'-'+str(argv.Month)+'-'+argv.Day+'-'+argv.hour+'-'+argv.mins+'.csv'))