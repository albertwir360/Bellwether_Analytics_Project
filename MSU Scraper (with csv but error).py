#!/usr/bin/env python
# coding: utf-8

# In[34]:


# This script pertains to the scraping of MSU technologies
import requests
from bs4 import BeautifulSoup
import re
import csv


# In[35]:


TAG_RE = re.compile(r'<[^>]+>')


# In[36]:


# check to make sure that the website link is good 
result = requests.get('http://msut.technologypublisher.com/searchresults.aspx?q=pharmaceutical')
# print(result.status_code)

#puts all the html into src variable
src= result.content
# print(src)

#create beautiful soup object in order to add more functionality to content variable 
soup = BeautifulSoup(src,'lxml')


# In[37]:


#python list to store all URL headers
atag = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a', href=True)
    atag.append(a_tag)

# gives all the urls in a python list with each element stored as strings 
urls = []
for i in atag:
    if i is not None:
        urls.append(i['href'])       
print(urls)
base_url = 'http://msut.technologypublisher.com/'

#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)
#print(final_urls)


# In[38]:


###################################################################################################
#After creating a means to get all the final urls create a final loop to make a request for every page and save the html
#TODO: only grab the inside descriptions of the span tag
descriptions = []
titles = []
for i in final_urls:
    res = requests.get(i)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')
    for i in final_soup.find_all("div", {"class":"c_tp_description"}):
        #text = i.find_all("span")
        #ptag = i.find_all('p')
        #title = i.find_all('h1')
        #titles.append(title)
        text = i.find_all('p')
        title = i.find_all('h1')
        titles.append(title)
        descriptions.append(text)

print(description)


# In[39]:


titles = [title for title in titles if title != []]
flattened_titles = [str(title) for subtitle in titles for title in subtitle]
flattened_titles = [title.strip("</h1>") for title in flattened_titles]
descriptions = [str(description) for description in descriptions if description != []]


# In[40]:


def remove_tags(text):
    return TAG_RE.sub('', text)


# In[41]:


descriptions = [remove_tags(text) for text in descriptions]


# In[42]:


mus_dict = {flattened_titles[i]: descriptions[i] for i in range(len(flattened_titles))}


# In[43]:


with open('msu.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in mus_dict.items():
            writer.writerow([key, value])

with open('msu.csv') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)
print(mus_dict)

