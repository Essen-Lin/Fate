import pandas as pd
import subprocess
import sys
import glob
import os
import numpy as np
 
path = '../input/tscs992.csv'
#所需的欄位
usecols = ['id','gender','year', 'birth_year','birth_month','birth_day','birth_hour']
df = pd.read_csv(path, usecols=usecols,encoding='utf-8')
nan = np.nan

data_size = len(df)


filename_all = [str(i) for i in list(df['id'])]
filename_all_2 = [str(i) for i in list(df['id'])]

filename_folder = glob.glob("../data/tscs992/*")
id_name_folder = []
run_list =[]

for i in filename_folder:
    name = os.path.split(i)
    id_name = name[1].partition('-')[0]
    id_name_folder.append(id_name)
    run_list.append(filename_all.index(id_name))

check_list = [ ]

for i in range(data_size):
    if (not np.isnan(df.at[i,'birth_month'])) and ( not np.isnan(df.at[i,'birth_day'])) and (not (df.at[i,'birth_hour'] is nan)):
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