import pandas as pd
import subprocess
import sys
import glob
import os
 
path = '../input/tscs992_with_birth_day_randomized.csv'
#所需的欄位
usecols = ['id','v1','year', 'v3y','v3m','birth_da','kv101_0']
df = pd.read_csv(path, usecols=usecols,encoding='Big5')

data_size = len(df)


filename_all = [str(i) for i in list(df['id'])]
filename_all_2 = [str(i) for i in list(df['id'])]

filename_folder = glob.glob("../data/1922_tscs992/*")
id_name_folder = []
run_list =[]

for i in filename_folder:
    name = os.path.split(i)
    id_name = name[1].partition('-')[0]
    id_name_folder.append(id_name)
    run_list.append(filename_all.index(id_name))

check_list = [ ]

for i in range(data_size):
    if ((df.at[i,'v3m']!='不知道或忘記') or (df.at[i,'v3m']!='不願意回答')) and (df.at[i,'birth_da'] > 0) and (df.at[i,'kv101_0']!="不適用"):
        check_list.append(i)

for i in run_list:
        check_list.remove(i)

if check_list != []:
    print("以下資料集 為執行失敗的index 並非id")
    print("將此list 放入run_tscs.py執行:",check_list)
    print("Data Size:",len(run_list))
else:
    print("已完成資料生成")
    print("Data Size:",len(run_list))
# print(len(check_list))