from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
from pprint import pprint
import numpy as np
import pandas as pd

my_url1 = 'https://www.kennet.com/'
my_url2 = 'https://www.kennet.com/who-we-are/'

#open connection, grab the html of page
uClient = uReq(my_url2)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, 'html.parser')
#print(page_soup.prettify())
container_a = page_soup.findAll('div', {'class':'team section '})
container_b = page_soup.findAll('div', {'class':'team section end'})
containers = container_a + container_b
container = containers[0]

#create dictionary of investment team members
#once created, can easily be converted for
#addition to SQL database, analysis as Pandas dataframe, etc...
name_list = []
location_list = []
for container in containers:
    name = container.h3.a.img['alt']
    location = container.h3.span.text
    name_list.append(name)
    location_list.append(location)
    
team_members = {}
team_members['names'] = name_list
team_members['locations'] = location_list

#create dataframe out of dictionary
df = pd.DataFrame.from_dict(team_members)
print('All Team Members')
print(df)
print('\n')

print('Bay Area Team Members')
print(df[df['locations'] == 'Silicon Valley'])
print('\n')

print('London Team Members')
print(df[df['locations'] == 'London'])
print('\n')



