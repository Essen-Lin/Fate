import pandas as pd
import subprocess
import sys
import numpy as np

path = '../input/tscs992.csv'
#所需的欄位
usecols = ['id','gender','year', 'birth_year','birth_month','birth_day','birth_hour']
df = pd.read_csv(path, usecols=usecols,encoding='utf-8')

print(df.head(45))
# data_list = [20, 61, 114, 150, 195, 271, 286, 335, 405, 406, 411, 465, 524, 570, 592, 635, 652, 700, 711, 768, 785, 796, 826, 964, 1062, 1134, 1563, 1610, 1624, 1632, 1725, 1836, 1844, 1869]
data_size = len(df)
# print(df)

# cnt = 0

def transform_hour(time):
    if time == '子時(23~01時)':
        return str(0)
    elif time == '丑時(01~03時)':
        return str(2)
    elif time == '寅時(03~05時)':
        return str(4)
    elif time == '卯時(05~07時)':
        return str(6)
    elif time == '辰時(07~09時)':
        return str(8)
    elif time == '巳時(09~11時)':
        return str(10)
    elif time == '午時(11~13時)':
        return str(12)
    elif time == '未時(13~15時)':
        return str(14)
    elif time == '申時(15~17時)':
        return str(16)
    elif time == '酉時(17~19時)':
        return str(18)
    elif time == '戍時(19~21時)':
        return str(20)
    elif time == '亥時(21~23時)':
        return str(22)

nan = np.nan  
for i in range(data_size):
    # print('id: ',str(df.at[i,'id']),'num: ',i)
    if df.at[i,'gender'] == '男':
        gender = 'm'
    elif df.at[i,'gender'] == '女':
        gender = 'w'
    # print(transform_hour(df.at[i,'birth_hour']))

    try:
        # print('M:   ', df.at[i,'birth_month'], 'nan:    ',np.isnan(df.at[i,'birth_month']))
        # print('D:   ', df.at[i,'birth_day'], 'nan:    ',np.isnan(df.at[i,'birth_day']))
        # print('H:   ', df.at[i,'birth_hour'], 'nan:    ',(df.at[i,'birth_hour'] is nan))
        # print(" ")
        
        if (not np.isnan(df.at[i,'birth_month'])) and ( not np.isnan(df.at[i,'birth_day'])) and (not (df.at[i,'birth_hour'] is nan)):

            print("python3.9 generate_database.py "+"-n "+ str(df.at[i,'id'])+
            " -g "+ gender+
            " -Y "+str(df.at[i, 'birth_year'])+
            " -M "+str(df.at[i,'birth_month'])+ 
            " -D "+str(int(df.at[i,'birth_day']))+ 
            " -o "+str(transform_hour(df.at[i,'birth_hour']))+
            " -v " +str(df.at[i,'year']))

            # subprocess.run(["python3.9","generate_database.py",
            # "-n",str(df.at[i,'id']),
            # "-g",gender,
            # "-Y", str(df.at[i, 'birth_year']),
            # "-M", str(int(df.at[i,'birth_month'])), 
            # "-D" ,str(int(df.at[i,'birth_day'])), 
            # "-o", str(transform_hour(df.at[i,'birth_hour'])),
            # "-v", str(df.at[i,'year']) ])
            # cnt+=1

    except:
        print("Error: not finish ouput file: ",i,'th file','/ id: ',str(df.at[i,'id']))
        sys.exit()

# print(cnt)