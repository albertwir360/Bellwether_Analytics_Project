#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
from bs4 import BeautifulSoup


# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://otm.illinois.edu/marketing-category/diagnostic-biological-testsassaysgenomicspretomics')
#print(result.status_code)

#puts all the html into src variable
src= result.content
#print(src)

#create beautiful soup object in order to add more functionality to content variable 
soup = BeautifulSoup(src,'lxml')


#python list to store all URL headers
atag = []
for td_tag in soup.find_all("h3"):
    a_tag = td_tag.find('a', href=True)
    atag.append(a_tag)

# gives all the urls in a python list with each element stored as strings 
urls = []
for i in atag:
    if i is not None:
        urls.append(i['href'])       
#print(urls)
base_url = 'https://otm.illinois.edu'

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
product_and_description = {}

for url in final_urls:
    res = requests.get(url)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')
    
    title = final_soup.find(id = "page-title").find_next_sibling('p').text
    overview = final_soup.find_all("div", class_ = 'field__item even')[1].text
    overview = overview.replace(u'\xa0', u' ') 
    titles.append(title)
    overviews.append(overview)

    #print(overview.findChildren())
    #break
    
    product_and_description[title] = overview
    
print(product_and_description)


# In[ ]:




