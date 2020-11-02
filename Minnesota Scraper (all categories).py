#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests
from bs4 import BeautifulSoup


# In[22]:


# biologics - 1195_biologics
# biomarkers - 1198_biomarkers
# cellular therapeutics - 1196_cellular-therapeutics
# diagnostic/imaging - 1211_diagnostics-imaging
# human health - 4451_human-health
# medical devices - 1214_medical-devices
# nueroscience - 5252_neuroscience
# pharma - 1197_pharmaceuticals

result = requests.get('http://license.umn.edu/categories/1181_life-sciences/1198_biomarkers?query=')

#check to make sure that the website link is good 
# print(result.status_code)


# In[14]:


#puts all the html into src variable
src= result.content
# print(src)


# In[15]:


#create beautiful soup object in order to add more functionality to content variable 
soup = BeautifulSoup(src,'lxml')


# In[16]:


#python list to store all URL headers
atag = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a', href=True)
    atag.append(a_tag)


# In[17]:


urls = []
for i in atag:
    if i is not None:
        urls.append(i['href'])       
# print(urls)
base_url = 'http://license.umn.edu/'


# In[18]:


#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)
# print(final_urls)


# In[19]:


#After creating a means to get all the final urls create a final loop to make a request for every page and save the html
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


# In[20]:


# clean titles
# remove the empty lists
titles = [title for title in titles if title != []]
# flatten list of lists into list and convert to string
flattened_titles = [str(title) for subtitle in titles for title in subtitle]
# remove the h1 tags
flattened_titles = [title.strip("</h1>") for title in flattened_titles]

# clean descriptions
# remove the empty lists and convert to string
descriptions = [str(description) for description in descriptions if description != []]


# In[21]:


# use dict comprehension to convert title and description lists to dict
minnesota_dict = {flattened_titles[i]: descriptions[i] for i in range(len(flattened_titles))}
print(minnesota_dict)


# In[ ]:




