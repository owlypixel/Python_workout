#! python3
import requests

response = requests.get('http://www.alienmovies.ca/html/scripts/aliens2.txt')
print(response.status_code)
print(response.text[:400])
response.raise_for_status()
file = open('Aliens_script.txt','wb')
for chunk in response.iter_content(100000):
	file.write(chunk)
file.close()
