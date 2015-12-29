# -*- coding: utf-8 -*-

# The model for the RentalProperty scraped item

import scrapy


class RentalProperty(scrapy.Item):
    property_num	= scrapy.Field()
    rent_amount 	= scrapy.Field()
    bond_amount		= scrapy.Field()
    street_address	= scrapy.Field()
    suburb			= scrapy.Field()
    postcode 		= scrapy.Field()
    num_bedrooms 	= scrapy.Field()
    num_bathrooms 	= scrapy.Field()
    num_carspaces	= scrapy.Field()
    property_type 	= scrapy.Field()
    url 			= scrapy.Field()
    description		= scrapy.Field()
    keywords		= scrapy.Field()
    date_available	= scrapy.Field()
    allowances		= scrapy.Field()
    other_features	= scrapy.Field()
    has_nbn			= scrapy.Field()
## http://www.nbnco.com.au/api/map/search.html?lat=-37.783408&lng=144.93114400000002&streetNumber=63&street=waltham%20street&suburb=flemington&postCode=3031&state=vic
