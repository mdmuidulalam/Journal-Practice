import scrapy

class StarTechSrapy(scrapy.Spider):
    name = 'startechlist'
    start_urls = [
        'https://www.startech.com.bd/',
    ]

    def parse(self, response):

        for menulink in response.css('nav ul li a::attr(href)').extract():
            print menulink