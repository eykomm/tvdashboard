# small scrapy script to extract the current menu from MedienBistro
# - by LBr 2017

import scrapy

# Define Fields for menu, price and day
class MenuItem(scrapy.Item):
	day = scrapy.Field()
	meal = scrapy.Field()
	price = scrapy.Field()

# Define class for website Spider
class MenuSpider(scrapy.Spider):
	name = 'menu'
	start_urls = ['http://www.caribbean-embassy.de/mittagstisch']

	# Extract table items from website - not working 100% yet
	def parse(self, response):
		rows = response.xpath('//table/tbody/tr')
		for row in rows:
			item = MenuItem()
			item['day'] = row.xpath('th/text()').extract()
			item['meal'] = row.xpath('td/text()').extract()
			item['price'] = row.xpath('td[2]/text()').extract()
			yield item
