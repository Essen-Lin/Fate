import pandas as pd
import subprocess
 
path = '/Users/essen/Library/Mobile Documents/com~apple~CloudDocs/Documents/交大/Fate/tscs992_with_birth_day_randomized.csv'
#所需的欄位
usecols = ['id','v1','year', 's.mon', 's.day', 's.hour','s.min']
df = pd.read_csv(path, usecols=usecols,encoding='Big5')
# print(df)
# print(df.head(10))

data_size = 100
for i in range(0,data_size):
    if df.at[i,'v1'] == '男':
        gender = 'm'
    elif df.at[i,'v1'] == '女':
        gender = 'w'
    # print(df.at[i,'id'])
    subprocess.run(["python3.9","generate_database.py","-n",str(df.at[i,'id']),"-g",gender,"-Y",str(df.at[i,'year']), "-M", str(df.at[i,'s.mon']), "-D" ,str(df.at[i,'s.day']), "-o", str(df.at[i,'s.hour']),"-m" ,str(df.at[i,'s.min'])])