import os
import pefile
import pandas as pd

dir_path = '/home/kali/Desktop/LAB4/MALWR'

res = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

print(res)

count = 0

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1

print("files: ", count)

def getApis(a):
    result = []
    for x in a.DIRECTORY_ENTRY_IMPORT:
        dll = x.dll.decode('utf-8')
        for y in x.imports:
            res.append(y.name.decode('utf-8'))
    
    return result

col = set()
apis = []

for filename in os.listdir(dir_path):
    f = os.path.join(dir_path, filename)
    #path = path + '/mal/' + file
    if os.path.isfile(f):
        peFile = pefile.PE(f)
        api = getApis(peFile)
        col.update(api)
        apis.append(api)

dict = {key: [] for key in col}

for x in apis:
    for y in col:
        if y in x:
            z = 1
            dict[y].append(z)
        else:
            z = 0
            dict[y].append(z)

print(dict)

data = pd.DataFrame.from_dict(dict)
data.to_csv('data.csv', index=True)