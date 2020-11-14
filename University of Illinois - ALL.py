#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


####Scrape for Therapeutics
# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://otm.illinois.edu/marketing-category/therapeutics')
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


# In[3]:


#After creating a means to get all the final urls create a final loop to make a request for every page and save the html
#TODO: only grab the inside descriptions of the span tag
product_and_description1 = {}
titles = []
overviews = []

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
    
    product_and_description1[title] = overview
    
#print(product_and_description1)
    


# In[4]:


#####Scrape for Diagnostics
#check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://otm.illinois.edu/marketing-category/diagnostic-hardwaresoftwaremedical-devices')
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
product_and_description2 = {}
titles = []
overviews = []

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
    
    product_and_description2[title] = overview
    
#print(product_and_description2)


# In[5]:


###Scrape for Non-Diagnostics
# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://otm.illinois.edu/marketing-category/non-diagnostic-hardwaresoftwaremedical-devices')
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
product_and_description3 = {}
titles = []
overviews = []

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
    
    product_and_description3[title] = overview
    
#print(product_and_description3)


# In[6]:


###Scrape for Diagnostic Bio
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
product_and_description4 = {}
titles = []
overviews = []

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
    
    product_and_description4[title] = overview
    
#print(product_and_description4)


# In[7]:


############FIX ME#########


###Scrape for Genomic
# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://otm.illinois.edu/marketing-category/genomicsproteomics')
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
product_and_description5 = {}
titles = []
overviews = []

for url in final_urls:
    res = requests.get(url)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')
    
    title = str(final_soup.find(id = "page-title").find_next_sibling('p'))
    overview = final_soup.find_all("div", class_ = 'field__item even')[1].text
    overview = overview.replace(u'\xa0', u' ') 
    
    #solve issue with "A Sustained Inhibition of Cancer Stem Cells via ..." being in <a> tag, not <p> tage

    if len(title) > 0:
        title = title.replace(u'<p>', u' ')
        title = title.replace(u'</p>', u' ')
        
            

    titles.append(title)
    overviews.append(overview)
    


    #print(overview.findChildren())
    #break
    
    product_and_description5[title] = overview
    
#print(product_and_description5)


# In[8]:


###Scrape for Human Systems
# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://otm.illinois.edu/marketing-category/human-systems')
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
product_and_description6 = {}
titles = []
overviews = []

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
    
    product_and_description6[title] = overview
    
#print(product_and_description6)


# In[9]:


###Scrape for Disease Type
# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://otm.illinois.edu/marketing-category/disease-type')
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
product_and_description7 = {}
titles = []
overviews = []

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
    
    product_and_description7[title] = overview
    
#print(product_and_description7)


# In[10]:


product_and_description = {**product_and_description1, **product_and_description2, **product_and_description3, **product_and_description4, **product_and_description5, **product_and_description6, **product_and_description7}
#print(product_and_description)


# In[11]:


#create one dictionary out of all dictionaries for all categories
product_and_description = {**product_and_description1, **product_and_description2, **product_and_description3, **product_and_description4, **product_and_description5, **product_and_description6, **product_and_description7}

#convert dict to csv file
import csv

with open('illinois2.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in product_and_description.items():
            writer.writerow([key, value])

with open('illinois2.csv') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)
print(product_and_description)


# In[ ]:




