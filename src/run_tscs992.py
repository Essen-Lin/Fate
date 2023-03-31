import pandas as pd
import subprocess
import sys
 
path = '../input/tscs992_with_birth_day_randomized.csv'
#所需的欄位
usecols = ['id','v1','year', 'v3y','v3m','birth_da','kv101_0']
df = pd.read_csv(path, usecols=usecols,encoding='Big5')

# print(df.head(10))
data_list = [560, 1228, 1573, 1786]
data_size = len(df)
print(df)

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
    
for i in data_list:
    print('id: ',str(df.at[i,'id']),'num: ',i)
    if df.at[i,'v1'] == '男':
        gender = 'm'
    elif df.at[i,'v1'] == '女':
        gender = 'w'
    print(transform_hour(df.at[i,'kv101_0']))

    try:
        if ((df.at[i,'v3m']!='不知道或忘記') or (df.at[i,'v3m']!='不願意回答')) and (df.at[i,'birth_da'] > 0) and (df.at[i,'kv101_0']!="不適用"):
            print("python3.9 generate_database.py "+"-n "+ str(df.at[i,'id'])+
            " -g "+ gender+
            " -Y "+str((df.at[i,'v3y']+1911))+
            " -M "+str(df.at[i,'v3m'])+ 
            " -D "+str(int(df.at[i,'birth_da']))+ 
            " -o "+str(transform_hour(df.at[i,'kv101_0'])))

            subprocess.run(["python3.9","generate_database.py",
            "-n",str(df.at[i,'id']),
            "-g",gender,
            "-Y", str((df.at[i,'v3y']+1911)),
            "-M", str(df.at[i,'v3m']), 
            "-D" ,str(int(df.at[i,'birth_da'])), 
            "-o", str(transform_hour(df.at[i,'kv101_0'])),
            "-v", str(df.at[i,'year']) ])



                  
    except:
        print("Error: not finish ouput file: ",i,'th file','/ id: ',str(df.at[i,'id']))
        sys.exit()