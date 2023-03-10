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
    name = driver.find_element(by=By.NAME,value='ion-input-0')
    name.send_keys(Name)

def set_birth_date(year,month,day,hours,mins):
    
    data_but_start = driver.find_element(by=By.XPATH, value='//*[@id="picker-input"]')
    data_but_start.click()
    time.sleep(5)
    # write script - years
    script_y ="document.getElementsByClassName('picker-years')[0].getElementsByClassName('picker-item picker-picked')[0].setAttribute('data-value'," + year + ")"
    # generate a alert via javascript
    driver.execute_script(script_y)
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-years > div.picker-cell__control.picker-cell__control--prev').click()
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-years > div.picker-cell__control.picker-cell__control--next').click()

    # write script - months
    script_m ="document.getElementsByClassName('picker-months')[0].getElementsByClassName('picker-item picker-picked')[0].setAttribute('data-value'," + month + ")"
    # generate a alert via javascript
    driver.execute_script(script_m)
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-months > div.picker-cell__control.picker-cell__control--prev').click()
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-months > div.picker-cell__control.picker-cell__control--next').click()

     # write script - days
    script_d ="document.getElementsByClassName('picker-days')[0].getElementsByClassName('picker-item picker-picked')[0].setAttribute('data-value'," + day+ ")"
    # generate a alert via javascript
    driver.execute_script(script_d)
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-days > div.picker-cell__control.picker-cell__control--prev').click()
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-days > div.picker-cell__control.picker-cell__control--next').click()

     # write script - hours 
    script_h ="document.getElementsByClassName('picker-hours')[0].getElementsByClassName('picker-item picker-picked')[0].setAttribute('data-value'," + hours + ")"
    # generate a alert via javascript
    driver.execute_script(script_h)
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-hours > div.picker-cell__control.picker-cell__control--prev').click()
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-hours > div.picker-cell__control.picker-cell__control--next').click()

    # write script - mins
    script_n ="document.getElementsByClassName('picker-minutes')[0].getElementsByClassName('picker-item picker-picked')[0].setAttribute('data-value'," + mins + ")"
    # generate a alert via javascript
    driver.execute_script(script_n)
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-minutes > div.picker-cell__control.picker-cell__control--prev').click()
    driver.find_element(by=By.CSS_SELECTOR, value='body > div.picker.picker-fixed.picker-open.picker-opened > div > div.picker-body > div > div.picker-cell.picker-minutes > div.picker-cell__control.picker-cell__control--next').click()
    time.sleep(2)

    driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div[3]/button[2]').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH,value='//*[@id="ion-overlay-4"]/div[2]/div/ion-list/ion-row[1]/ion-col/ion-button').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH,value='//*[@id="main"]/div[1]/ion-content/div[1]/ion-list/div[2]/ion-item/ion-label').click()
    
datas = []
#'??????/??????'=0,'??????'=1,
fieldnames = ['??????/??????','??????','??????','????????????', '????????????', # '??????' = 1,'??????' =2 '????????????' = 3, '????????????' = 4
'??????1','??????1????????????','??????1????????????','??????1????????????', #'??????1'=5,'??????1????????????'=6,'??????1????????????'=7,'??????1????????????'=8
'??????2','??????2????????????','??????2????????????','??????2????????????', #'??????2'=9,'??????2????????????'=10,'??????2????????????'=11,'??????2????????????'=12
'????????????','????????????','????????????',   #'????????????' = 13 ,'????????????' = 14 ,'????????????' = 15 
'????????????','????????????','????????????',   #'????????????' = 16 ,'????????????' = 17 ,'????????????' = 18 
'????????????','????????????','????????????',   #'????????????' = 19 ,'????????????' = 20 ,'????????????' = 21
'??????','??????','??????','??????', #'??????' = 22 ,'??????' =23 ,'??????' =24 ,'??????' =25 
'????????????','????????????',   #'????????????' = 26 ,'????????????' = 27
'????????????','????????????',   #'????????????' = 28 ,'????????????' = 29
'??????','??????????????????','??????????????????','??????????????????', # '??????' = 30 ,'??????????????????' = 31 ,'??????????????????' = 32 ,'??????????????????' = 33
'??????','??????????????????','??????????????????','??????????????????', # '??????' = 34 ,'??????????????????' = 35 ,'??????????????????' = 36 ,'??????????????????' = 37
'??????','??????????????????','??????????????????','??????????????????', # '??????' = 38 ,'??????????????????' = 39 ,'??????????????????' = 40 ,'??????????????????' = 41
'??????','??????????????????','??????????????????','??????????????????', # '??????' = 42 ,'??????????????????' = 43 ,'??????????????????' = 44 ,'??????????????????' = 45
'boshi'] # 'boshi' = 46
datas.append(fieldnames)

def crawl(url,decade):
    soup = BeautifulSoup(url, "html.parser")
    ganzhi = soup.find_all('td')

    ganzhi_new = []
    ganzhi_new.append(ganzhi[11])
    ganzhi_new.append(ganzhi[10])
    ganzhi_new.append(ganzhi[9])
    ganzhi_new.append(ganzhi[7])
    ganzhi_new.append(ganzhi[4])
    ganzhi_new.append(ganzhi[0])
    ganzhi_new.append(ganzhi[1])
    ganzhi_new.append(ganzhi[2])
    ganzhi_new.append(ganzhi[3])
    ganzhi_new.append(ganzhi[6])
    ganzhi_new.append(ganzhi[8])
    ganzhi_new.append(ganzhi[12])


    for index in range(0,len(ganzhi_new)):
        # if index != 5:
        i = ganzhi_new[index]
        try:         
            chart_unit_ganzhi = i.find(class_ = 'chart-unit-ganzhi')
            detail_datas = [' ']*47
            detail_datas [0] = decade
            detail_datas[1]= chart_unit_ganzhi.text[0]
            detail_datas[2]= chart_unit_ganzhi.text[1]

        except:
            pass

        try:
            chart_unit_decade_palace = i.find(class_ = 'chart-unit-decade-palace')
            detail_datas[3] = chart_unit_decade_palace.text
        except:
            pass

        try:
            chart_unit_natal_palace = i.find(class_ ='chart-unit-natal-palace')
            detail_datas[4]= chart_unit_natal_palace.text
        except:
            pass
        
        try:
            north_star_unit = i.find(class_ = 'north-star-unit')
            detail_datas[5]= north_star_unit.text[:2]
        except:
            pass

        try:
            natal_morph = i.select_one('div.north-star-unit > span.natal-morph')
            detail_datas[6]= natal_morph.text
        except:
            pass

        try:
            decade_morph = i.select_one('div.north-star-unit > span.decade-morph')
            detail_datas[7]= decade_morph.text
        except:
            pass

        try:
            taisui_morph = i.select_one('div.north-star-unit > span.taisui-morph')
            detail_datas[8]= taisui_morph.text
        except:
            pass

        try:
            south_star_unit = i.find(class_ = 'south-star-unit')
            if (detail_datas[5]==' '):
                detail_datas[5] = south_star_unit.text[:2]
            else:
                detail_datas[9] = south_star_unit.text[:2]
        except:
            pass

        try:
            s_natal_morph = i.select_one('div.south-star-unit > span.natal-morph')
            if (detail_datas[9]== ' '):
                detail_datas[6]= s_natal_morph.text
            else:
                detail_datas[10]= s_natal_morph.text
        except:
            pass

        try:
            s_decade_morph = i.select_one('div.south-star-unit > span.decade-morph')
            if (detail_datas[9]==' '):
                detail_datas[7]= s_decade_morph.text
            else:
                detail_datas[11]= s_decade_morph.text
        except:
            pass

        try:
            s_taisui_morph = i.select_one('div.south-star-unit > span.taisui-morph')
            if (detail_datas[9]==' '):
                detail_datas[8]= s_taisui_morph.text
            else:
                detail_datas[12]= s_taisui_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                detail_datas[13] = 1
            if(suppot_star_text.find('??????')+1):
                detail_datas[16] = 1  
            if(suppot_star_text.find('??????')+1):
                detail_datas[19] = 1  
        except:
            pass
        
        try:
            decade_sup_star_unit_text = str(i.find(class_ = 'decade-sup-star-unit'))
            if(decade_sup_star_unit_text.find('??????')+1):
                detail_datas[14] = 1
            if(decade_sup_star_unit_text.find('??????')+1):
                detail_datas[17] = 1
            if(decade_sup_star_unit_text.find('??????')+1):
                detail_datas[20] = 1
        except:
            pass

        try:
            taisui_sup_star_unit_text = str(i.find(class_ = 'taisui-sup-star-unit'))
            if(taisui_sup_star_unit_text.find('??????')+1):
                detail_datas[15] = 1
            if(taisui_sup_star_unit_text.find('??????')+1):
                detail_datas[18] = 1
            if(taisui_sup_star_unit_text.find('??????')+1):
                detail_datas[21] = 1
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                detail_datas[22] = 1
            if(suppot_star_text.find('??????')+1):
                detail_datas[23] = 1
        except:
            pass

        try:
            suppot_star_text = str(i.find_all(class_ = 'support-star-unit'))
            if(suppot_star_text.find('??????')+1):
                detail_datas[24] = 1
            if(suppot_star_text.find('??????')+1):
                detail_datas[25] = 1
        except:
            pass

        try:
            suppot_star_text = str(i.find_all(class_ = 'extra-star-unit'))
            if(suppot_star_text.find('??????')+1):
                detail_datas[26] = 1
        except:
            pass


        try:
            taisui_sup_star_unit_text = str(i.find(class_ = 'taisui-sup-star-unit'))
            if(taisui_sup_star_unit_text.find('??????')+1):
                detail_datas[27] = 1
        except:
            pass

        try:
            suppot_star_text = str(i.find_all(class_ = 'extra-star-unit'))
            if(suppot_star_text.find('??????')+1):
                detail_datas[28] = 1
        except:
            pass


        try:
            taisui_sup_star_unit_text = str(i.find(class_ = 'taisui-sup-star-unit'))
            if(taisui_sup_star_unit_text.find('??????')+1):
                detail_datas[29] = 1
        except:
            pass

## ??????
        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                detail_datas[30] = 1
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                natal_morph = i.select_one('div.support-star-unit > span.natal-morph')
                detail_datas[31]= natal_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                decade_morph = i.select_one('div.support-star-unit > span.decade-morph')
                detail_datas[32]= decade_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                taisui_morph = i.select_one('div.support-star-unit > span.taisui-morph')
                detail_datas[33]= taisui_morph.text
        except:
            pass


        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                detail_datas[34] = 1
                natal_morph = i.select_one('div.support-star-unit > span.natal-morph')
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                natal_morph = i.select_one('div.support-star-unit > span.natal-morph')
                detail_datas[35]= natal_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                decade_morph = i.select_one('div.support-star-unit > span.decade-morph')
                detail_datas[36]= decade_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                taisui_morph = i.select_one('div.support-star-unit > span.taisui-morph')
                detail_datas[37]= taisui_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                detail_datas[38] = 1
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                natal_morph = i.select_one('div.support-star-unit > span.natal-morph')
                detail_datas[39]= natal_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                decade_morph = i.select_one('div.support-star-unit > span.decade-morph')
                detail_datas[40]= decade_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                taisui_morph = i.select_one('div.support-star-unit > span.taisui-morph')
                detail_datas[41]= taisui_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                detail_datas[42] = 1
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                natal_morph = i.select_one('div.support-star-unit > span.natal-morph')
                detail_datas[43]= natal_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                decade_morph = i.select_one('div.support-star-unit > span.decade-morph')
                detail_datas[44]= decade_morph.text
        except:
            pass

        try:
            suppot_star_text = str(i.find_all('span',{'class':'support-star-text'}))
            if(suppot_star_text.find('??????')+1):
                taisui_morph = i.select_one('div.support-star-unit > span.taisui-morph')
                detail_datas[45]= taisui_morph.text
        except:
            pass


        try:
            chart_unit_boshi = i.find(class_ = 'chart-unit-boshi')
            detail_datas[46]=chart_unit_boshi.text
        except:
            pass

        datas.append(detail_datas)

def write_to_csv(filename):
    crawl(driver.page_source,'??????')
    for i in range(1,11):
        shen_xpath = '//*[@id="root"]/ion-app/div[2]/ion-footer/div/div[1]/div['+str(i)+']'
        shen_source = str(i)+'???'    
        driver.find_element(by=By.XPATH,value=shen_xpath).click()
        crawl(driver.page_source,shen_source)

        for i in range(1,11):
            year_xpath = '//*[@id="root"]/ion-app/div[2]/ion-footer/div/div[2]/div['+str(i)+']/span[1]'
            year_source = driver.find_element(by=By.XPATH,value=year_xpath).text
            driver.find_element(by=By.XPATH,value=year_xpath).click()
            crawl(driver.page_source,year_source)

    with open(filename, 'w', newline='',encoding='big5') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(datas)


	
if __name__ == "__main__":
    # Initialize  parser (Chrome) - Download the version of used chrome in the same path, and change the PATH
    PATH = "/Users/essen/LocalData/NCTU/Fate/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get("https://ziweigonglue1013.firebaseapp.com/login")
    #?????????????????? - ????????????
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

    #????????????(w/m) ??????????????????
    # Name = 'Essen'
    # Gender = 'w'
    usrname_gender(argv.Name,argv.Gender)

    #????????????????????????
    # year = '1996'
    # input_month = 7
    # month = str(input_month-1)
    # day = '10'
    # hour = '15'
    # min = '30'

    month = str(argv.Month-1)
    set_birth_date(argv.Year,month,argv.Day,argv.hour,argv.mins) 

    time.sleep(2)
    write_to_csv('../data/1922_tscs992/'+argv.Name+'-'+(argv.Year+'-'+str(argv.Month)+'-'+argv.Day+'-'+argv.hour+'-'+argv.mins+'.csv'))
    driver.quit()