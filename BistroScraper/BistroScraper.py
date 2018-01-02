# small scrapy script to extract the current menu from MedienBistro www.carribean-embassy.de/mittagstisch
# - by LBr 17
#
# Usage/Setup:
# > pip install scrapy
# > scrapy runspider <scriptname.py> -o <outputfile.csv>
# or run '> scrapy shell' for command line shell and fire commands manually for debugging

import scrapy

# Define Fields for menu, price and day
class MenuItem(scrapy.Item):
	day = scrapy.Field()
	meal = scrapy.Field()
	price = scrapy.Field()

# Define class for website spider
class MenuSpider(scrapy.Spider):
	name = 'menu'
	start_urls = ['http://www.caribbean-embassy.de/mittagstisch']

	# Extract table items from website - not working 100% yet
	def parse(self, response):
		rows = response.xpath('//table/tbody/tr')
		for row in rows:
			item = MenuItem()
			item['day'] =  self.extractText(row,'th//text()')
			item['meal'] = self.extractText(row,'td[1]//text()')
			item['price'] = self.extractText(row,'td[2]//text()')
			yield item

	def extractText(self,row,xpathSelector):
		extractedLines = row.xpath(xpathSelector).extract()
		extractedText = " ".join(extractedLines)
		cleanedText = extractedText.strip()
		return cleanedText
