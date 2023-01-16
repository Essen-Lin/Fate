
# generate "Essen" 的命盤
python3.9 generate_database.py -n Essen -g woman -Y 1996 -M 7 -D 10 -o 15 -m 30
# 批次執行來自 tscs992 並且生成命盤
# path = '../input/tscs992_with_birth_day_randomized.csv'
python3 run_tscs992.py
# debug and confirm "run-tscs992.py" 是否有檔案沒跑道並且生成沒跑成功的檔案
python3 debug_tscs992.py
