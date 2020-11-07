#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://www.warf.org/search-results/?searchwp=&search-technology=1&s_tech_category=medical-imaging&date-range-start=&date-range-end=')
#print(result.status_code)

#puts all the html into src variable
src= result.content
#print(src)

#create beautiful soup object in order to add more functionality to content variable 
soup_wisco = BeautifulSoup(src,'lxml')


#python list to store all URLs
atag = []
for h2_tag in soup_wisco.find_all("h2"):
    a_tag = h2_tag.find('a', href=True)
    atag.append(a_tag)

# gives all the urls in a python list with each element stored as strings 
urls = []
for i in atag:
    if i is not None:
        urls.append(i['href'])       
#print(urls)
base_url = ''

#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)
#print(final_urls)

#After creating a means to get all the final urls create a final loop to make a request for every page and save the html
#TODO: only grab the inside descriptions of the span tag
titles = []
overviews = []
wisco_product_and_descriptions = {}

for url in final_urls:
    res = requests.get(url)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')

    #key assumption: overview remains first section-content
    overview = final_soup.find_all("div", class_ = "section-content")[0].text
    overview = overview.replace(u'\n', u' ') 

    title = final_soup.find("div", class_ = "heading").text
    titles.append(title)
    overviews.append(overview)
    
    #add to dict
    wisco_product_and_descriptions[title] = overview
    
print(wisco_product_and_descriptions)


# In[ ]:




