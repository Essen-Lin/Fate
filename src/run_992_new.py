import pandas as pd
import subprocess
import sys
import numpy as np

path = '../input/tscs992.csv'
#所需的欄位
usecols = ['id','gender','year', 'birth_year','birth_month','birth_day','birth_hour']
df = pd.read_csv(path, usecols=usecols,encoding='utf-8')

# print(df.head(20)) 
data_list = [1078]
data_size = len(df)
# print(df)

# cnt = 0

def transform_hour(time):
    if time == '23-1時(子時)':
        return str(0)
    elif time == '1-3時(丑時)':
        return str(2)
    elif time == '3-5時(寅時)':
        return str(4)
    elif time == '5-7時(卯時)':
        return str(6)
    elif time == '7-9時(辰時)':
        return str(8)
    elif time == '9-11時(巳時)':
        return str(10)
    elif time == '11-13時(午時)':
        return str(12)
    elif time == '13-15時(未時)':
        return str(14)
    elif time == '15-17時(申時)':
        return str(16)
    elif time == '17-19時(酉時)':
        return str(18)
    elif time == '19-21時(戌時)':
        return str(20)
    elif time == '21-23時(亥時)':
        return str(22)

nan = np.nan  
for i in data_list:
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

            subprocess.run(["python3.9","generate_database.py",
            "-n",str(df.at[i,'id']),
            "-g",gender,
            "-Y", str(df.at[i, 'birth_year']),
            "-M", str(int(df.at[i,'birth_month'])), 
            "-D" ,str(int(df.at[i,'birth_day'])), 
            "-o", str(transform_hour(df.at[i,'birth_hour'])),
            "-v", str(df.at[i,'year']) ])
            # cnt+=1

    except:
        print("Error: not finish ouput file: ",i,'th file','/ id: ',str(df.at[i,'id']))
        sys.exit()

# print(cnt)