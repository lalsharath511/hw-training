import gzip
import io
import requests
import re
from parsel import Selector
import json
class Ebby():
    def __init__(self):
        self.headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
		}
    def parse(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        selector = Selector(text=response.text)
        try:
                names = selector.xpath('//div[@class="rng-bio-account-content"]//h1/text()').extract_first().split(' ')
                try:
                    agent_phone = selector.xpath('//section[@class="rng-bio-account-details"]//a/text()').extract()[0].replace(' ','')
                except:
                    agent_phone="" 
                try:
                    agent_email=selector.xpath('//section[@class="rng-bio-account-details"]//a/text()').extract()[1].strip()
                except:
                    agent_email=""
                office = selector.xpath('//section[@class="rng-bio-account-content-office"]//strong/text()').extract_first().split('|')[0].strip()
                addres = selector.xpath(
                 '//section[@class="rng-bio-account-content-office"]//div[2]/text()').extract_first().strip().replace(',', '').split(' ')
                title=selector.xpath('//section[@class="rng-bio-account-content-office"]//div//span/text()').extract_first()
                if title==None:
                    title=""
                image_url=selector.xpath('//div[@class="rng-bio-account-slider"]//img/@src').extract_first()
                disc=selector.xpath('//section[contains(@class,"description")]//p/text()').extract()
                if disc ==[]:
                    disc=selector.xpath('//div[contains(@id,"bioAccountContentDesc")]/div/text()').extract()
                    if disc ==[]:
                        disc=selector.xpath('//section/div[contains(@id,"bioAccountContentDesc")]/div/text()').extract()
                        if disc==[]:
                            disc==selector.xpath('//div[contains(@id,"body-text-1-preview-6890-2214002")]/p/text()').extract()
                            
                website=selector.xpath('//a[contains(text(),"Visit my site")]/@href').extract_first()
                if website==None:
                    website=""
                    
                adrs = ""
                for adr in addres[:-3]:
                    adrs += adr+" "
                address=adrs.strip()
                city=addres[-3]
                zip_code=addres[-1]
                state=addres[-2]
               
                    
        except:
                names = selector.xpath('//p[@class="rng-agent-profile-contact-name"]/text()').extract_first().replace("\n","").strip(" ").split(" ")
                image_url=selector.xpath('//main//img/@src').extract_first()
                title=selector.xpath('//p[@class="rng-agent-profile-contact-name"]/span/text()').extract_first(),
                disc=selector.xpath('//div[@id="body-text-1-preview-6890-4157397"]/p/text()').extract_first()
                office=""
                address=""
                city=""
                zip_code=""
                state=""
                agent_phone=selector.xpath('//ul[@class="rng-preferred-partner-contact-info"]/li/a/text()').extract_first()
                agent_email=""
                website=""
        
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
        
        details = {
			'country': 'United states',
			'first_name': first_name,
			'middle_name': middle_name,
			'last_name': last_name,
			'image_url': image_url,
			'title': title,
			'office_name': office,
			'description': disc,
			'languages': [],
			'address': address,
			'city': city,
			'zip_code': zip_code,
			'state': state,
			'agent_phone': agent_phone,
			'office_phone': "",
			'social': "",
			'website': website,
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
                