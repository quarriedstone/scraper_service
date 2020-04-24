import scrapy
from ..items import AmazonProduct
import logging
import ast
import random

class AmazonScraper(scrapy.Spider):
    logging.getLogger('scrapy').propagate = False
    name = "amazon_scraper"  

    # Headers to fix 503 service unavailable error
    # Spoof headers to force servers to think that request coming from browser ;)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'} 

    def start_requests(self): 
        # starting urls for scraping
        urls = ["https://www.amazon.com/s?k={}&ref=nb_sb_noss_2".format(self.category)]
        for url in urls: yield scrapy.Request(url = url, callback = self.parse, headers = self.headers)

    def parse(self, response):
        self.no_pages = int(response.xpath("//ul[@class='a-pagination']/li[@class='a-disabled']/text()").getall()[-1])
        return self.parse_all(response)

        
    def parse_all(self, response):
        if response.xpath("//div[@id='nav-logo']/a").get() is None:
            yield scrapy.Request(url=response.url, callback = self.parse_all, headers = self.headers, dont_filter=True)

        self.no_pages -= 1

        products = response.xpath("//a[@class='a-link-normal a-text-normal']").xpath("@href").getall()
        for product in products:
            final_url = response.urljoin(product) 
            yield scrapy.Request(url=final_url, callback = self.parse_product, headers = self.headers)
                   
        if(self.no_pages > 0):
            next_page_url = response.xpath("//ul[@class='a-pagination']/li[@class='a-last']/a").xpath("@href").get()
            final_url = response.urljoin(next_page_url)
            yield scrapy.Request(url = final_url, callback = self.parse_all, headers = self.headers)

    def parse_product(self, response):
        if response.xpath("//div[@id='nav-logo']/a").get() is None:
            yield scrapy.Request(url=response.url, callback = self.parse_product, headers = self.headers, dont_filter=True)

        url = response.request.url

        title = response.xpath("//span[@id='productTitle']//text()").get() or response.xpath("//h1[@id='title']//text()").get()
        rating = response.xpath("//div[@id='averageCustomerReviews_feature_div']").xpath("//span[@class='a-icon-alt']//text()").get()

        price = response.xpath("//span[@id='priceblock_ourprice']//text()") or response.xpath("//span[@id='priceblock_dealprice']//text()")
        
        if len(price) > 1: price = price[1].get()
        elif len(price) == 1: price = price[0].get()
        else : price = price.get()

        colour = response.xpath("//div[@id='variation_color_name']/div/span[@class='selection']//text()").get() or "not defined"
        description_raw = response.xpath("//div[@id='featurebullets_feature_div']//span[@class='a-list-item']//text()").getall()

        description = []
        for description_temp in description_raw:
            description.append(description_temp.strip())
        brand = response.xpath("//a[@id='bylineInfo']//text()").get() or "not specified"
        reviews = response.xpath("//div[@class='a-expander-content reviewText review-text-content a-expander-partial-collapse-content']/span//text()").getall()

        img_url = response.xpath("//img[@id='landingImage']/@data-old-hires").get() or response.xpath("//img[@id='imgBlkFront']/@src").get()
        
        if img_url is None:
            img_url = response.xpath("//img[@id='landingImage']/@data-a-dynamic-image").get()
            if img_url is None: 
                return
            else:
                img_url = list(ast.literal_eval(img_url).keys())
        else:
            img_url = [img_url]

 
        website = 'Amazon'  
        
        title = title.strip() if title is not None else 'not defined'.strip()
        rating = rating.strip() if rating is not None else 'not defined'.strip()
        if price is None:
            return
        else:
            price = price.strip()
        colour = colour.strip()
        brand = brand.strip() if brand is not None else 'not defined'.strip()

        yield AmazonProduct(title=title, rating=rating, price=price, colour=colour, description=description, reviews=reviews, brand=brand, image_urls=img_url, website=website, url=url)
