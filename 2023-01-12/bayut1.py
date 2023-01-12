
import requests
import re
from parsel import Selector
import json
from datetime import date

class Bayut():
    def __init__(self):
        self.headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
		}
        self.count=0
    def parse(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        selector = Selector(text=response.text)
        link=[*set(selector.xpath("//a[@aria-label='Listing link']/@href").extract())]
        for url in link:
            url=f'https://www.bayut.sa{url}'
            self.parse_property(url)
        link2=selector.xpath("//a[@title='Next']/@href").extract_first()
        
        url1=f'https://www.bayut.sa{link2}'
        self.parse(url1)
        
            
    def parse_property(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        selector = Selector(text=response.text)
        url_id = re.findall("[0-9]", url)
        amenities=[*set(selector.xpath("//h3[contains(text(),'Features / Amenities')]/following-sibling::div//span/text()").extract())]
        price_per=selector.xpath("//span[@aria-label='Frequency']/text()").extract_first()
        if price_per is None:
            price_per = "" 
        listing_availability=selector.xpath("//span[@aria-label='Inactive property banner']/text()").extract_first()
        if listing_availability is None:
            listing=True
        else:
            listing=False
            
            
        disc=selector.xpath("//div[@aria-label='Property description']//div[@dir='auto']/span/text()").extract()
        disc=",".join(disc)
        number_of_photos=selector.xpath("//div[contains(text(),'Photos')]/text()").extract_first()
        number_of_photos = re.findall("[0-9]", number_of_photos)
        number_of_photos = "".join(number_of_photos)
        user_id=selector.xpath("//a[@aria-label='View all properties']/@href").extract_first()
        user_id1=re.findall("[0-9]", user_id)
        print(type(user_id1))
        user_id="".join(user_id1)
        phone_no=selector.xpath("/html/body/script[1]/text()").extract_first()
        phone_no1=[*set(re.findall('mobilePhoneNumber.*?",',phone_no))][0]
        primaryPhoneNumber=[*set(re.findall('primaryPhoneNumber.*?",',phone_no))][0]

        phone_number=[]
        ph_no=""
        ph_no1=""
        for ph in primaryPhoneNumber:
            if ph.isdigit():
                ph_no1=ph_no1+ph
        phone_number.append(ph_no1)
        
        for ph in phone_no1:
            if ph.isdigit():
                ph_no=ph_no+ph
                
        phone_number.append(ph_no)

        phone_number=','.join(phone_number)
        
        
        data2={
            "reference_number": selector.xpath("//span[@aria-label='Reference']/text()").extract_first(),
            "url": url,
            "broker_display_name": selector.xpath("//span[@aria-label='Agency name']/text()").extract_first(),
            "broker": (selector.xpath("//span[@aria-label='Agency name']/text()").extract_first()).upper(),
            "category": selector.xpath("//span[@aria-label='Purpose']/text()").extract_first(),
            "category_url": selector.xpath("//div[@aria-label='Breadcrumb']/a[2]/@href").extract_first(),
            "title": selector.xpath("//div[@aria-label='Property overview']/h1/text()").extract_first(),
            "description": disc,
            "location": selector.xpath("//div[@aria-label='Property header']/text()").extract_first(),
            "price": selector.xpath("//span[@aria-label='Price']/text()").extract_first().replace(",",""),
            "currency": selector.xpath("//span[@aria-label='Currency']/text()").extract_first(),
            "bedrooms": selector.xpath("//span[@aria-label='Beds']/span/text()").extract_first(),
            "bathrooms": selector.xpath("//span[@aria-label='Baths']/span/text()").extract_first(),
            "furnished": "",
            "amenities": amenities,
            "details": selector.xpath("//span[@aria-label='Area']//span//span/text()").extract_first(),
            "agent_name": selector.xpath("//span[@aria-label='Agent name']/text()").extract_first(),
            "number_of_photos": number_of_photos,
            "user_id": user_id,
            "phone_number": phone_number,
            "date": f'{date.today()}',
            "property_type": selector.xpath("//span[@aria-label='Type']/text()").extract_first(),
            "published_at": selector.xpath("//span[@aria-label='Reactivated date']/text()").extract_first(),
            "listing_availability": listing,
            "id": "".join(url_id)
            }
        dict_str = json.dumps(data2)
        json_file = open('coldwellbanker.json','a')
        json_file.write(dict_str+"\n")

        

    
        
        
path = 'https://www.bayut.sa/en/ksa/properties-for-sale/'
ebby = Bayut()
ebby.parse(path)
