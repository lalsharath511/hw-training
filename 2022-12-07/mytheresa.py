import requests
from parsel import Selector
import json

data = []


def crawl(link1):
    res = link1

    if res.status_code != 200:
        raise Exception('Failed to load page')
    text = res.text
    selector = Selector(text=text)
    product = selector.xpath("//div[@class='main']")
    sizes_details = selector.xpath("//div[@class='product-shop'] //ul[@class='sizes'] //span/text()").getall()
    sizes = []
    for size in sizes_details:
        size = size.replace("/", " ").strip(" ").split("  ")
        for i in size:
            sizes.append(i)
    listing_price = product.xpath(
        "//div[@class='product-shop'] //span[@class='regular-price'] //span[@class='price']/text()").get()
    if listing_price == None:
        listing_price = product.xpath(
            "//div[@class='product-shop'] //p[@class='old-price'] //span[@class='price']/text()").get()
    dict1 = {
        "breadcrumbs": product.xpath("//div[@class='breadcrumbs'] //span/text()").getall()[0:-1],
        "image_url": f"https:{product.css('img.gallery-image').xpath('@src').get()}",
        "brand": product.xpath("//a[@class='text-000000']/text()").get(),
        "product_name": product.xpath("//div[@class='product-name'] //span/text()").get(),
        "listing_price": listing_price,
        "offer_price": product.xpath(
            "//div[@class='product-shop'] //p[@class='special-price'] //span[@class='price']/text()").get(),
        "discount": product.xpath(
            "//div[@class='product-shop'] //span[@class='price-reduction-notice']/text()").get(),
        "product_id": product.xpath("//span[@class='h1']/text()").get()[-9:],
        "sizes": sizes,
        "description": (str(product.css('p.pa1-rmm.product-description::text').get())) + ' '.join(
            product.xpath("//li[@class='pa1-rmm']/text()").getall()),
        "other_images": product.css('img.gallery-image').xpath('@data-src').getall()
    }
    data.append(dict1)
    with open("sample.json", "w") as outfile:
        json.dump(data, outfile)
    return

def mytheresa(next_page):
    res = requests.get(next_page,
                       headers={
                           "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
    if res.status_code != 200:
        raise Exception('Failed to load page')
    text = res.text
    selector = Selector(text=text)
    temp = 0
    for link in selector.css('li.item a').xpath("@href"):
        try:
            link1 = requests.get(link.get(), headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
            if temp == link.get():
                continue
            else:
                crawl(link1)
                temp = link.get()

        except:
            continue

    next_page = selector.css('li.next a').xpath('@href').get()
    if next_page is not None:
        mytheresa(next_page)


mytheresa('https://www.mytheresa.com/int_en/clothing.html')

