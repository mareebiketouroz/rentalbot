import scrapy

from rentals.items import RentalProperty

class RentalsSpider(scrapy.Spider):
    name = 'rentals'
    allowed_domains = ['www.realestate.com.au']
    start_urls = ['http://www.realestate.com.au/rent/with-studio-bedrooms-between-100-400-in-fitzroy%2c+vic+3065%3b+fitzroy+north%2c+vic+3068%3b+brunswick%2c+vic+3056%3b+north+melbourne%2c+vic+3051%3b+melbourne+city+-+greater+region%2c+vic%3b+docklands%2c+vic+3008%3b+carlton%2c+vic+3053%3b+kensington%2c+vic+3031%3b+flemington%2c+vic+3031/list-1?activeSort=price-asc']

    """
    for each rental link
        get rental property url, save to item object
        follow rental property url, retrieve other properties, save to item object
    also follow pagination
    return list of items
    """

    def parse(self, response):
        for href in response.css("header > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_property_page)
        next_page = response.css(".nextLink > a::attr('href')")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse) # recursive loop

    def parse_property_page(self, response):
        item = RentalProperty()
        item['url'] = response.url
        item['property_num'] = response.xpath('//span[@class="property_id"]/text()').re('Property No\. (\d+)')[0]
        item['rent_amount'] = response.xpath('//p[@class="priceText"]/text()')[0].extract()
        item['bond_amount'] = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Bond")]/span/text()').extract()
        item['street_address'] = response.xpath('//h3[@class="address"]/text()').extract()
        item['suburb']            = None
        item['postcode']        = None
        item['num_bedrooms']    = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Bedrooms")]/span/text()').extract()
        item['num_bathrooms']    = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Bathrooms")]/span/text()').extract()
        item['num_carspaces']    = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Bond")]/span/text()').extract()
        if len(item['num_carspaces']) == 0: item['num_carspaces'] = '0'
        item['property_type']    = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Property Type")]/span/text()').extract()
        item['description']        = "\n".join(response.xpath('//p[@class="body"]/text()').extract())
        item['keywords']        = None
        item['date_available']    = response.xpath('//div[@class="available_date"]/span/text()').extract()
        item['allowances']        = None
        item['other_features']    = None
        yield item
