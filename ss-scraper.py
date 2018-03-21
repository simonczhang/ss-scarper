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
#create container list for all members
container_a = page_soup.findAll('div', {'class':'team section '})
container_b = page_soup.findAll('div', {'class':'team section end'})
containers = container_a + container_b

#loop through each person and grab the title, name, location and add to list
name_list = []
location_list = []
title_list = []
for container in containers:
    #get title from link to inner page for each profile
    name_link = container.h3.a['href']
    uClient2 = uReq(name_link)
    page_html2 = uClient2.read()
    uClient2.close()
    page_soup2 = soup(page_html2, 'html.parser')
    content = page_soup2.findAll('div', {'id':'main'})
    content = content[0]
    title, loc = content.h2.text.split(',')
    #get name, location for each profile
    name = container.h3.a.img['alt']
    location = container.h3.span.text
    #add to lists
    name_list.append(name)
    location_list.append(location)
    title_list.append(title)
    
#create dictionary of investment team members
#once created, can easily be converted for
#addition to SQL database, analysis as Pandas dataframe, etc...
team_members = {}
team_members['names'] = name_list
team_members['locations'] = location_list
team_members['title'] = title_list

#create dataframe out of dictionary to find bay area members, london members
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