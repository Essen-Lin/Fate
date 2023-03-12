import pandas as pd
import subprocess
import sys
 
path = '../input/tscs992_with_birth_day_randomized.csv'
#所需的欄位
usecols = ['id','v1','year', 's.mon', 's.day', 's.hour','s.min']
df = pd.read_csv(path, usecols=usecols,encoding='Big5')

# print(df.head(10))
data_list = [541, 810, 1645, 1766]
data_size = len(df)
print(data_size)
for i in data_list:
    print('id: ',str(df.at[i,'id']),'num: ',i)
    if df.at[i,'v1'] == '男':
        gender = 'm'
    elif df.at[i,'v1'] == '女':
        gender = 'w'
    # print(df.at[i,'id'])
    try:
        subprocess.run(["python3.9","generate_database.py",
        "-n",str(df.at[i,'id']),
        "-g",gender,
        "-Y",str(df.at[i,'year']),
        "-M", str(df.at[i,'s.mon']), 
        "-D" ,str(df.at[i,'s.day']), 
        "-o", str(df.at[i,'s.hour']),
        "-m" ,str(df.at[i,'s.min'])])
    except:
        print("Error: not finish ouput file: ",i,'th file','/ id: ',str(df.at[i,'id']))
        sys.exit()