import json
import os
import re
 
 
rootdir = r'2023-01-10/guarantee_2023_01_05.json'
 
for files in os.scandir(rootdir):
 
        with open(files, "r") as file:
            json_data = json.load(file)
            extracted  = re.findall(("city"),json_data)
            print(extracted)
            
