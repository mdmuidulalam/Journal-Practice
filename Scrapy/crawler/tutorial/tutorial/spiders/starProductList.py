import scrapy

class StarTechSrapy(scrapy.Spider):
    name = 'startechlist'
    start_urls = [
        'https://www.startech.com.bd/laptop-notebook/laptop',
    ]

    def parse(self, response):

        for navItem in response.css('nav ul li'):
            yield {
                'category': navItem.css('a::text').extract_first(),
                'link': navItem.css('a::attr(href)').extract_first()
            }