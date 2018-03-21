from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url1 = 'https://www.kennet.com/'
my_url2 = 'https://www.kennet.com/who-we-are/'

#open connection, grab the html of page
uClient = uReq(my_url2)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')
#print(page_soup.prettify())
