#!/usr/bin/env python
# coding: utf-8

# In[15]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
import csv
import numpy as np 


# In[2]:


TAG_RE = re.compile(r'<[^>]+>')


# In[3]:


# biologics - 1195_biologics
# biomarkers - 1198_biomarkers
# cellular therapeutics - 1196_cellular-therapeutics
# diagnostic imaging - 1211_diagnostics-imaging
# human health - 4451_human-health
# medical devices - 1214_medical-devices
# nueroscience - 5252_neuroscience
# pharma - 1197_pharmaceuticals

result = requests.get('http://license.umn.edu/categories/1181_life-sciences/1195_biologics?query=')
# print(result.status_code)


# In[4]:


#puts all the html into src variable
src= result.content
# print(src)


# In[5]:


#create beautiful soup object in order to add more functionality to content variable 
soup = BeautifulSoup(src,'lxml')


# In[6]:


#python list to store all URL headers
atag = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a', href=True)
    atag.append(a_tag)


# In[7]:


# gives all the urls in a python list with each element stored as strings 
urls = []
for i in atag:
    if i is not None:
        urls.append(i['href'])       
# print(urls)
base_url = 'http://license.umn.edu/'


# In[8]:


#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)
# print(final_urls)


# In[9]:


#After creating a means to get all the final urls create a final loop to make a request for every page and save the html
#TODO: only grab the inside descriptions of the span tag
descriptions = []
titles = []

for i in final_urls:
    res = requests.get(i)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')
    # print(len(final_soup.find_all('div', class_='technology')))
    for i in final_soup.find_all('div', class_='technology'):
        # print(i)
        text = i.find_all('p')
        title = i.find_all('h1')
        titles.append(title)
        descriptions.append(text)


# In[10]:


# clean titles
# remove the empty lists
titles = [title for title in titles if title != []]
# flatten list of lists into list and convert to string
flattened_titles = [str(title) for subtitle in titles for title in subtitle]
# remove the h1 tags
flattened_titles = [title.strip("</h1>") for title in flattened_titles]


# In[11]:


# clean descriptions
# remove the empty lists and convert to string
descriptions = [str(description) for description in descriptions if description != []]


# In[12]:


def remove_tags(text):
    return TAG_RE.sub('', text)


# In[13]:


descriptions = [remove_tags(text) for text in descriptions]


# In[14]:


# cleaning to remove new lines and spaces
# descriptions = [[[descr.replace("\n", " ") for text in descr] for descr in description] for description in descriptions]
# descriptions = [descr for subdescr in descriptions for descr in subdescr]

# print(descriptions[5])

# create dict to map title of article to description

# use dict comprehension to convert title and description lists to dict
minnesota_dict = {flattened_titles[i]: descriptions[i] for i in range(len(flattened_titles))}

# print(minnesota_dict)

with open('mine.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in minnesota_dict.items():
            writer.writerow([key, value])

with open('mine.csv') as csv_file:
    reader = csv.reader(csv_file)
    # {}
    for row in reader:
        print(row)
        row = np.array(row)
        #print(row.shape)
        writer = csv.writer(csv_file)


# In[ ]:




