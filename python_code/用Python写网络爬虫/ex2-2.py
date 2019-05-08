import lxml.html
import urllib.request

def scrape(html):
	tree = lxml.html.fromstring(html)
	td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
	area = td.text_content() 
	return area

if __name__ == '__main__':
	req = urllib.request.urlopen('http://example.webscraping.com/places/default/view/Aland-Islands-2')
	html = req.read()
	print(scrape(html))
