import pandas as pd
import subprocess
import sys
import glob
import os
 
path = '../input/tscs992_with_birth_day_randomized.csv'
#所需的欄位
usecols = ['id','v1','year', 's.mon', 's.day', 's.hour','s.min']
df = pd.read_csv(path, usecols=usecols,encoding='Big5')


filename_all = [str(i) for i in list(df['id'])]
filename_all_2 = [str(i) for i in list(df['id'])]

filename_folder = glob.glob("../data/1952_tscs992/*")
id_name_folder = []
run_list =[]

for i in filename_folder:
    name = os.path.split(i)
    id_name = name[1].partition('-')[0]
    id_name_folder.append(id_name)
    filename_all_2.remove(id_name)

# print(filename_all)

for i in filename_all_2:
    # print(filename_all.index(i))
    run_list.append(i)

print(run_list)