#! python3
# -*- coding: utf-8 -*-

import sys
import os
import openpyxl
import requests
import json
import csv

# Settings section
requests_num = 20

print("Making api request")
r = requests.get('https://randomuser.me/api/?results=' + str(requests_num) + '?nat=us,dk,fr,gb')
print(r.text)
parsed_json = json.loads(r.text)

print("Creating a new output file")
outputFile = open('output.csv', 'w')
outputWriter = csv.writer(outputFile)

for idx, i in enumerate(parsed_json['results']):
	outputWriter.writerow(i['name']['first'])
#	print(idx)
#	print('A' + str(idx + 1))    
#	print(parsed_json['results'])
#	print i['name']['first']
print("Saving csv")
outputFile.close()

print("Done!")
