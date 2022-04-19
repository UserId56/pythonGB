import linecache
import sys
param = sys.argv
with open('DB_shop.txt', 'r') as file:
    lines = file.readlines
    # print(lines[0])
    max_index = 3
    start = 0 if len(param) == 1 else int(param[1])
    stop = max_index if len(param) < 3 else int(param[2])
    for i in range(start, stop):
        print(linecache.getline('DB_shop.txt', i-1))
print(start, stop)
