import urllib.request
from urllib.error import URLError, HTTPError,ContentTooShortError
def download(url):
	print("Downloading:",url)

	try:
		html = urllib.request.urlopen(url).read()
	except (URLError,HTTPError,ContentTooShortError) as e:
		print("Download error", e.reason)
		html = None
	
	return html 

# html = download("https://books.xingzhi.wiki")

# print(html)


def download1(url, num_retries = 2):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
             # recursively retry 5xx HTTP errors
             	return download1(url, num_retries - 1)
    return html

html = download1("http://httpstat.us/500")

print(html)