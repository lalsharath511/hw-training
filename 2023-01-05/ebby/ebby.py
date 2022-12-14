import requests
from parsel import Selector
import csv
class Ebby():

	def __init__(self):
		self.fields = ['country','first_name','last_name','image_url','title', 'office_name', 'description', 'address', 'city', 'zip_code', 'state', 'agent_phone','office_phone', 'social','website', 'agent_email', 'profile_url']
		self.headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
		}
		with open('ebby.csv','w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=self.fields)
			writer.writeheader()


	def parse(self,url):
		response = requests.get(url=url, headers=self.headers)
		print(response.status_code)
		selector = Selector(text=response.text)

		names = selector.xpath('//div[@class="rng-bio-account-content"]//h1/text()').extract_first().split(' ')
		
		description = selector.xpath('//section[contains(@class,"description")]//p/text()')
		contact = selector.xpath('//section[@class="rng-bio-account-details"]//a/text()').extract()
		office = selector.xpath('//section[@class="rng-bio-account-content-office"]//strong/text()').extract_first().split('|')
		address = selector.xpath('//section[@class="rng-bio-account-content-office"]//div[2]/text()').extract_first().strip().replace(',','').split(' ')

		first_name = names[0]
		if len(names) == 3:
			middle_name = names[1]
			last_name = names[2]
		else:
			middle_name = ""
			last_name = names[1]
		adrs = ""
		for adr in address[:-3]:
			adrs += adr+" "

		
		
		details = {
		'country': 'United states',
		'first_name': first_name,
		'middle_name': middle_name,
		'last_name': last_name,
		'image_url': selector.xpath('//div[@class="rng-bio-account-slider"]//img/@src').extract_first(),
		'title': selector.xpath('//section[@class="rng-bio-account-content-office"]//div//span/text()').extract_first(),
		'office_name': office[0].strip(),
		'description': selector.xpath('//section[contains(@class,"description")]//p/text()').extract(),
		'languages': "",
		'address': adrs.strip(),
		'city': address[-3],
		'zip': address[-1],
		'state': address[-2],
		'agent_phone': contact[0].replace(' ',''),
		'office_phone': "",
		'social': "",
		'website': selector.xpath('//a[contains(text(),"Visit my site")]/@href').extract_first(),
		'agent_email': contact[1].strip(),
		'profile_url': url,
		}
		with open('ebby.csv','a') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=self.fields)
			writer.writerow(details) 
    def parse_link(self, url):
        response = requests.get(url=url, headers=self.headers)
		if response.status_code != 200:
            raise Exception("Error")
		else:
      
		# for page in range(2,145):
		# 	next_page = f"https://www.ebby.com/roster/agents/{page}"
		# 	parse(next_page)
url = 'file:///home/czone/.cache/.fr-qFx8cC/sitemapbio%20(3).xml'
ebby = Ebby()
ebby.parse_link(url)