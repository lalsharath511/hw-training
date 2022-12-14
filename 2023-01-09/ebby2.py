import gzip
import io
import requests
from parsel import Selector
import json
class Ebby():
	def __init__(self):
		self.headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
		}
		
	def parse(self,url):
			
		response = requests.get(url=url, headers=self.headers)
		print(response.status_code)
		selector = Selector(text=response.text)
		try:names = selector.xpath('//div[@class="rng-bio-account-content"]//h1/text()').extract_first().split(' ')
			contact = selector.xpath('//section[@class="rng-bio-account-details"]//a/text()').extract()
			office = selector.xpath('//section[@class="rng-bio-account-content-office"]//strong/text()').extract_first().split('|')
			address = selector.xpath('//section[@class="rng-bio-account-content-office"]//div[2]/text()').extract_first().strip().replace(',','').split(' ')
		except:
      			names = selector.xpath('//p[@class="rng-agent-profile-contact-name"]/text()').extract_first().strip("\n").strip()
  				image_url=selector.xpath('//main//img/@src').extract_first()
		# description = selector.xpath('//section[contains(@class,"description")]//p/text()')
		
		if not contact:
			agent_phone =''
			agent_email =""
		else:
			agent_phone=contact[0].replace(' ','')
			agent_email=contact[1].strip()
		
		first_name = names[0]
		if len(names) == 3:
			middle_name = names[1]
			last_name = names[2]
		elif len(names)==2:
			middle_name = ""
			last_name = names[1]
		else:
			middle_name = ""
			last_name=""
		adrs = ""
		for adr in address[:-3]:
			adrs += adr+" "
		details = {
			'country': 'United states',
			'first_name': first_name,
			'middle_name': middle_name,
			'last_name': last_name,
			'image_url': selector.xpath('//main//img/@src').extract_first(),
			'title': selector.xpath('//p[@class="rng-agent-profile-contact-name"]/span/text()').extract_first(),
			'office_name': office[0].strip(),
			'description': selector.xpath('//section[contains(@class,"description")]//p/text()').extract(),
			'languages': "",
			'address': adrs.strip(),
			'city': address[-3],
			'zip_code': address[-1],
			'state': address[-2],
			'agent_phone': agent_phone,
			'office_phone': "",
			'social': "",
			'website': selector.xpath('//a[contains(text(),"Visit my site")]/@href').extract_first(),
			'agent_email':  agent_email,
			'profile_url': url,
			}
		dict_str = json.dumps(details)
		json_file = open('ebby.json','a')
		json_file.write(dict_str+"\n")
			
		
	def parse_link(self,path):
		links=[]
		with gzip.open(path, 'rb') as gz_reader_filehandle:
			with io.TextIOWrapper(gz_reader_filehandle, encoding='utf-8') as gz_decoder_obj:
				gz_file_contents = gz_decoder_obj.read()
				a=gz_file_contents.split("loc>")
				for i in a:
					if 'https://www.ebby.com/bio/' in i:
						links.append(i.strip("</"))
		for link in links:
			print(link)
			self.parse(link)
path = 'sitemapbio.xml.gz'
ebby = Ebby()
ebby.parse_link(path)