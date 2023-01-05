from parsel import Selector
import requests
import csv


class mytheresaScraper:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        with open('result.csv', 'w') as csv_file:
            csv_file.write(
                "breadcrumbs,image_url,brand,product_name,listing_price,offer_price,discount,product_id,sizes,description,other_images\n")

    def crawl(self, new_url):
        response = new_url
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        product = selector.xpath("//div[@class='main']")
        sizes_details = selector.xpath("//div[@class='product-shop'] //ul[@class='sizes'] //span/text()").extract()
        sizes = []
        for size in sizes_details:
            size = size.replace("/", " ").strip(" ").split("  ")
            for value in size:
                sizes.append(value)
        listing_price = product.xpath(
            "//div[@class='product-shop'] //span[@class='regular-price'] //span[@class='price']/text()").extract_first()
        if listing_price == None:
            listing_price = product.xpath(
                "//div[@class='product-shop'] //p[@class='old-price'] //span[@class='price']/text()").extract_first()
        dict1 = {
            "breadcrumbs": product.xpath("//div[@class='breadcrumbs'] //span/text()").extract()[0:-1],
            "image_url": f"https:{product.css('img.gallery-image').xpath('@src').extract_first()}",
            "brand": product.xpath("//a[@class='text-000000']/text()").extract_first(),
            "product_name": product.xpath("//div[@class='product-name'] //span/text()").extract_first(),
            "listing_price": listing_price,
            "offer_price": product.xpath(
                "//div[@class='product-shop'] //p[@class='special-price'] //span[@class='price']/text()").extract_first(),
            "discount": product.xpath(
                "//div[@class='product-shop'] //span[@class='price-reduction-notice']/text()").extract_first(),
            "product_id": product.xpath("//span[@class='h1']/text()").extract_first()[-9:],
            "sizes": sizes,
            "description": (str(product.xpath(
                '//p[contains(@class, "product-description")]/text()').extract_first())) + ' '.join(
                product.xpath("//li[@class='pa1-rmm']/text()").extract()),
            "other_images": selector.xpath('//img[contains(@class,"gallery-image")]/@data-src').extract()
        }
        with open('result.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=dict1.keys())
            writer.writerow(dict1)

        return

    def mytheresa(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            raise Exception('Failed to load page')

        selector = Selector(text=response.text)
        temp = 0
        for link in selector.xpath('//a[contains(@class,"product-image")]/@href'):
            try:
                new_url = requests.get(link.extract(), headers=self.headers)
                if temp == link.extract():
                    continue
                else:
                    self.crawl(new_url)
                    temp = link.extract_first()
            except:
                continue
        next_page = selector.xpath('//li[contains(@class,"next")]/a/@href').extract_first()
        if next_page is not None:
            self.mytheresa(next_page)


url = 'https://www.mytheresa.com/int_en/men/shoes.html'
obj = mytheresaScraper()
obj.mytheresa(url)
