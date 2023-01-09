# import trafilatura
# from trafilatura import sitemaps
import json

# links = sitemaps.sitemap_search('https://www.coldwellbanker.com/sitemap_brokers_index.xml')
# # print(links)
from parsel import Selector
import requests

class ColdwellBanker:

    def __init__(self):
        self.fields = ['first_name','last_name','image_url','title', 'description', 'address', 'city', 'zip_code', 'state', 'agent_phone', 'agent_email', 'profile_url']
        self.list1=0
        self.headers = {
        "user-agent": "Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    def crawl(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        # a=selector.xpath("//div[@class='media__content']/h1/text()").extract_first().strip("\n").strip(" ")
        b=selector.xpath("//a[contains(@class,'agent-link')]/@href").extract()
        for url in b:
            self.agent_details(url)
        # details = {
		
		# 	"first_name": first_name,
		# 	"last_name": last_name,
		# 	"image_url": image_url,
		# 	"title": selector.xpath('//h2[@itemprop="jobTitle"]/text()').extract_first().strip(),
		# 	"description": description,
		# 	"address": selector.xpath('//div[@itemprop="streetAddress"]/text()').extract_first(),
		# 	"city": selector.xpath('//span[@itemprop="addressLocality"]/text()').extract_first(),
		# 	"zip_code": selector.xpath('//span[@itemprop="postalCode"]/text()').extract_first(),
		# 	"state": selector.xpath('//span[@itemprop="addressRegion"]/text()').extract_first(),
		# 	"agent_phone": selector.xpath('//a[contains(@class,"o-phone-number")]/text()').extract_first(),
		# 	"agent_email": selector.xpath('//a[contains(@class,"listing-item__agent-email-address")]/text()').extract_first(),
		# 	"profile_url": url,
		# 	}
        # self.list1=self.list1+b
        
    def sitemap(self,url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        sitemap_url=selector.xpath("//sitemap/loc/text()").extract()
        for url in sitemap_url:
            self.coldwellbanker(url)
            break
            
            
          
    def coldwellbanker(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        # print(response.text)
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        office_url=selector.xpath("//url/loc/text()")[1].extract()
        print(office_url)
        self.crawl(office_url)
    def agent_details(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        print(selector)
        details = {
		
			"first_name": first_name,
			"last_name": last_name,
			"image_url": image_url,
			"title": selector.xpath('//h2[@itemprop="jobTitle"]/text()').extract_first().strip(),
			"description": description,
			"address": selector.xpath('//div[@itemprop="streetAddress"]/text()').extract_first(),
			"city": selector.xpath('//span[@itemprop="addressLocality"]/text()').extract_first(),
			"zip_code": selector.xpath('//span[@itemprop="postalCode"]/text()').extract_first(),
			"state": selector.xpath('//span[@itemprop="addressRegion"]/text()').extract_first(),
			"agent_phone": selector.xpath('//a[contains(@class,"o-phone-number")]/text()').extract_first(),
			"agent_email": selector.xpath('//a[contains(@class,"listing-item__agent-email-address")]/text()').extract_first(),
			"profile_url": url,
			}
        self.list1=self.list1+b
        
        
url= 'https://www.coldwellbanker.com/sitemap_brokers_index.xml'     
obj = ColdwellBanker()
obj.sitemap(url)
        
    
        # b=[l for l in a if'office' in l]
        # print(b)
        
        # print(response.text)
        # a=selector.xpath('//article[contains(@class,"rng-agent-roster-agent-card js-sort-item")]/a/@href')
        # print(a)
        # for link in selector.xpath('//article[contains(@class,"rng-agent-roster-agent-card js-sort-item")]/a/@href'):
        #     print(link.text)https://www.coldwellbanker.com/coldwell-banker-1st-choice-realty-1127c/sitemap.xml

            # mylines = [] 
            # new=[]
            # with open ('a.txt', 'rt') as myfile: 
            #     for myline in myfile:
            #         myline=myline.split("loc>")
            #         mylines.append(myline)
                    
            # for i in myline:
            #     if 'https://www.coldwellbanker.com' in i:
            #         i=i.strip("</").strip(" ")
            #         new.append(i)
            # 





            
            
#         # add its contents to mylines.
# # print(new)
# import requests
# from parsel import Selector
# import csv
# class ColdwellBanker:
# 	def __init__(self):
# 		self.fields = ['first_name','last_name','image_url','title', 'description', 'address', 'city', 'zip_code', 'state', 'agent_phone', 'agent_email', 'profile_url']
# 		self.headers = {
# 		"user-agent": "Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
# 		}
# 		with open('coldwellbanker.csv', 'w') as csvfile:
# 			writer = csv.DictWriter(csvfile, fieldnames=self.fields)
# 			writer.writeheader()
# 	def parse(self,url):

# 		response = requests.get(url=url, headers=self.headers)
# 		if response.status_code != 200:
# 			raise Exception("Page Not Found")
# 		else:
# 			selector = Selector(text=response.text)
# 			image = selector.xpath('//div[@id="agentphoto"]//img/@src').extract_first()
# 			image_url = f"https:{image}"
# 			description = selector.xpath('//div[@itemprop="description"]/text()').extract_first()
# 			if description is None or description == ' ':
# 				description1 = selector.xpath('//div[@itemprop="description"]//p/text()').extract_first()
# 				description = description1
# 				if description1 is None or description1 == ' ':
# 					description2 = selector.xpath('//div[@itemprop="description"]//p//span/text()').extract_first()
# 					description = description2
# 					if description2 is None or description2 == ' ':
# 						description = "No description Available"
			
# 			for name in selector.xpath('//h1[@itemprop="name"]/text()').extract():
# 				first_name = name.split(' ')[0]
# 				last_name = name.split(' ')[1]
# 			details = {
		
# 			"first_name": first_name,
# 			"last_name": last_name,
# 			"image_url": image_url,
# 			"title": selector.xpath('//h2[@itemprop="jobTitle"]/text()').extract_first().strip(),
# 			"description": description,
# 			"address": selector.xpath('//div[@itemprop="streetAddress"]/text()').extract_first(),
# 			"city": selector.xpath('//span[@itemprop="addressLocality"]/text()').extract_first(),
# 			"zip_code": selector.xpath('//span[@itemprop="postalCode"]/text()').extract_first(),
# 			"state": selector.xpath('//span[@itemprop="addressRegion"]/text()').extract_first(),
# 			"agent_phone": selector.xpath('//a[contains(@class,"o-phone-number")]/text()').extract_first(),
# 			"agent_email": selector.xpath('//a[contains(@class,"listing-item__agent-email-address")]/text()').extract_first(),
# 			"profile_url": url,
# 			}
# 			with open('alliebeth2.csv','a') as csvfile:
# 				writer = csv.DictWriter(csvfile,fieldnames=self.fields)
# 				writer.writerow(details)
    
#     def sitemap(self,url):
#         response = requests.get(url=url, headers=self.headers)
#         if response.status_code != 200:
#             raise Exception('Failed to load page')
#         selector = Selector(text=response.text)
#         sitemap_url=selector.xpath("//sitemap/loc/text()").extract()
#         for url in sitemap_url:
           
            
            
# 	def parse_link(self,url):
# 		response = requests.get(url=url, headers=self.headers)
# 		if response.status_code != 200:
# 			raise Exception("Page Not Found")
# 		selector = Selector(text=response.text)
# 		links = selector.xpath('//a[@class="url"]/@href').extract()
# 		for link in links:
# 			try:
# 				alliebeth.parse(link)
# 			except:
# 				continue
# 		next_page = selector.xpath('//a[@aria-label="Next Page"]/@href').extract_first()
# 		if next_page is not None:
# 			next_page = f"https://www.alliebeth.com{next_page}"
# 			alliebeth.parse_link(next_page)

# url = 'https://www.coldwellbanker.com/sitemap_brokers_index.xml'
# alliebeth = ColdwellBanker()
# alliebeth.sitemap(url)