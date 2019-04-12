import scrapy

class Description:
    ParagraphDescription = []
    ItemDescription = []

class ProductData:
    Category = []
    Name = ''
    BrandName = ''
    Availability = ''
    RegularPrice = 0
    MainPrice = 0
    ShortDescription = []
    Description = Description()
    Specification = { }

def ProcessStringToSave(info):
    if info is None:
        return info

    info = info.encode('ascii','ignore').strip()
    removechars = ['\r', '\n']    
    for rc in removechars:
        info = info.replace(rc, '')
    return info

def ProcessIntToSave(info):
    if info is None:
        return info

    info = info.encode('ascii','ignore').replace(',', '').strip()
    removechars = ['\r', '\n']    
    for rc in removechars:
        info = info.replace(rc, '')
    try:
        return int(info)
    except ValueError:
        return info

class StarTechSrapy(scrapy.Spider):
    name = 'startech'
    start_urls = [
        'https://www.startech.com.bd/laptop-notebook/laptop?page=3',
    ]

    def parse(self, response):
        # count = 0
        # for productLink in response.css('div.main-content div.product-thumb div.product-info h4.product-name a::attr(href)').extract():
        #     yield response.follow(productLink, self.parseProduct)
        #     count += 1
        #     print count, productLink

        for productListLink in response.css('div.bottom-bar ul.pagination *::attr(href)').extract():
            yield response.follow(productListLink, self.parse)
        
    
    def parseProduct(self, response):
        # print '\n'
        # print 'xxxxxxxxxx Output xxxxxxxxxx'
        # print '\n'

        data = ProductData()
         
        for category in response.css('ul.breadcrumb li a::text').extract():
            data.Category.append(ProcessStringToSave(category))

        data.Name = ProcessStringToSave(response.css('div.product-title h1::text').extract_first())

        for item in response.css('div.short-info ul li'):
            if item.css('b::text').extract_first().strip() == 'Brand:':
                data.BrandName = ProcessStringToSave(item.css('a span::text').extract_first())

            if item.css('b::text').extract_first().strip() == 'Availability:':
                data.Availability = ProcessStringToSave(item.css('span::text').extract_first())

        data.RegularPrice = ProcessIntToSave(response.css('div.regular-price::text').extract_first())
        data.MainPrice = ProcessIntToSave(response.css('div.price-wrap ins::text').extract_first()) 

        for item in response.css('div.short-description li::text').extract():
            data.ShortDescription.append(ProcessStringToSave(item))

        for item in response.css('div[itemprop="description"] ul li::text').extract():
            data.Description.ItemDescription.append(ProcessStringToSave(item))

        for item in response.css('div[itemprop="description"] p::text').extract():
            data.Description.ParagraphDescription.append(ProcessStringToSave(item))

        tableHead = []
        for item in response.css('table.data-table thead tr td::text').extract():
            th = ProcessStringToSave(item)
            tableHead.append(th)
            data.Specification[th] = { }

        i=0
        for item in response.css('table.data-table tbody'):
            for sp in item.css('tr'):
                data.Specification[tableHead[i]][ProcessStringToSave(sp.css('td.name::text').extract_first())] = ProcessStringToSave(sp.css('td.value::text').extract_first())
            i += 1

        # print data.Specification["Basic Information"]["Processor"]
        # print data.Specification["Input Devices"]["Optical Drive"]
        # print data.Specification["Physical Specification"]["Weight"]
        # print tableHead
        # print data.Category
        # print data.Name
        # print data.BrandName
        # print data.Availability
        # print 'MainPrice = ', data.MainPrice
        # print 'RegularPrice = ', data.RegularPrice
        # print data.ShortDescription
        # print data.Description.ItemDescription
        # print data.Description.ParagraphDescription

        filename = 'startech/startech.txt'
        with open(filename, 'a') as f:
            f.write(data.Name + '\n')

        # print '\n'
        # print 'xxxxxxxxxx Output xxxxxxxxxx'
        # print '\n'