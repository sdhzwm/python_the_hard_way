import lxml.html
from lxml import etree

import urllib.request

def scrape(html):
	tree = lxml.html.fromstring(html)
	table = tree.xpath('//table')[0]
	print(table.getchildren()) # 所有子元素
	print(table.getprevious()) # 所有兄弟元素
	print(table.getnext()) #
	print(table.getparent())# 父元素

	area = tree.xpath('//tr[@id="places_area__row"]/td[@class="w2p_fw"]/text()')[0]	
	img =  tree.xpath('//tr[@id="places_national_flag__row"]/td[@class="w2p_fw"]/img/@src')[0]
	print(img)
	return area

if __name__ == '__main__':
	req = urllib.request.urlopen('http://example.webscraping.com/places/default/view/Aland-Islands-2')
	html = req.read()
	print(scrape(html))
