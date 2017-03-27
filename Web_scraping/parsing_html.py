import bs4, requests

electric_query = 'https://www.rabota.kharkov.ua/vacancies/search/page1?keyword=%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%B8%D0%BA'

def get_salaries(page):
	response = requests.get(page)
	response.raise_for_status()
	soup_obj = bs4.BeautifulSoup(response.text, 'html.parser')
	elems = soup_obj.select('.pay')
	for el in elems:
		print(el.text.strip())

get_salaries(electric_query)