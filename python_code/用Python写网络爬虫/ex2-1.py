from bs4 import BeautifulSoup
import urllib.request

def scrape(html):
	soup = BeautifulSoup(html) 	
	tr = soup.find(attrs={'id':'header'})
	td = tr.find(attrs={'class':'page-header'})  
	area = td.text 
	return area

if __name__ == '__main__':
	req = urllib.request.urlopen('http://example.webscraping.com/view/United-Kingdom-239')
	html = req.read()
	print(scrape(html))
