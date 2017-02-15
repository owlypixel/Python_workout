#! python3

#pip install openpyxl
#pip install requests
import sys
import os
import openpyxl
import requests
import json

# Settings section
requests_num = 20

# Making api request
print("Making api request")
r = requests.get('https://randomuser.me/api/?results=' + str(requests_num))
parsed_json = json.loads(r.text)

# Creating a new workbook
print("Creating a new workbook")
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
sheet.title = "Randomusers"

# Filling in our sheet with data from the request
for idx, i in enumerate(parsed_json['results']):
	sheet['A' + str(idx + 1)] = i['name']['first']    

# Saving a workbook
print("Saving workbook")
wb.save("randomusers.xlsx")
print("Done!")

