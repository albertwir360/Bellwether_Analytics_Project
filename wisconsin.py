import requests
from bs4 import BeautifulSoup

###Scrape Diagnostic Assay
#check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://www.warf.org/search-results/?s_tech_category=diagnostic-assays&searchwp=&search-technology=1')

#puts all the html into src variable
src= result.content

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
base_url = ''

#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)

    
#After creating a means to get all the final urls create a final loop to make a request for every page and save the html
titles = []
overviews = []

wisco_product_and_descriptions1 = {}

for url in final_urls:
    res = requests.get(url)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')

    #key assumption: overview remains first section-content
    overview = final_soup.find_all("div", class_ = "section-content")[0].text
    overview = overview.replace(u'\n', u' ') 
    overview = overview.replace(u'\xa0', u' ') 

    title = final_soup.find("div", class_ = "heading").text
    titles.append(title)
    overviews.append(overview)
    
    #add to dict
    wisco_product_and_descriptions1[title] = overview
    

###Scrape Wisconsin Drug Discovery
# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://www.warf.org/search-results/?s_tech_category=drug-discovery&searchwp=&search-technology=1')

#puts all the html into src variable
src= result.content

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
base_url = ''

#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)

#After creating a means to get all the final urls create a final loop to make a request for every page and save the html
titles = []
overviews = []

wisco_product_and_descriptions2 = {}

for url in final_urls:
    res = requests.get(url)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')

    #key assumption: overview remains first section-content
    overview = final_soup.find_all("div", class_ = "section-content")[0].text
    overview = overview.replace(u'\n', u' ') 
    overview = overview.replace(u'\xa0', u' ') 
    title = final_soup.find("div", class_ = "heading").text
    titles.append(title)
    overviews.append(overview)
    
    #add to dict
    wisco_product_and_descriptions2[title] = overview
    

###Scrape Medical Devices
# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://www.warf.org/search-results/?searchwp=&search-technology=1&s_tech_category=medical-devices&date-range-start=&date-range-end=')

#puts all the html into src variable
src= result.content

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
base_url = ''

#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)

#After creating a means to get all the final urls create a final loop to make a request for every page and save the html
titles = []
overviews = []

wisco_product_and_descriptions3 = {}

for url in final_urls:
    res = requests.get(url)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')

    #key assumption: overview remains first section-content
    overview = final_soup.find_all("div", class_ = "section-content")[0].text
    overview = overview.replace(u'\n', u' ') 
    overview = overview.replace(u'\xa0', u' ') 
    title = final_soup.find("div", class_ = "heading").text
    titles.append(title)
    overviews.append(overview)
    
    #add to dict
    wisco_product_and_descriptions3[title] = overview
    

###Scrape Medical Imaging
# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://www.warf.org/search-results/?searchwp=&search-technology=1&s_tech_category=medical-imaging&date-range-start=&date-range-end=')

#puts all the html into src variable
src= result.content

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
base_url = ''

#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)

#After creating a means to get all the final urls create a final loop to make a request for every page and save the html
titles = []
overviews = []
wisco_product_and_descriptions4 = {}

for url in final_urls:
    res = requests.get(url)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')

    #key assumption: overview remains first section-content
    overview = final_soup.find_all("div", class_ = "section-content")[0].text
    overview = overview.replace(u'\n', u' ') 
    overview = overview.replace(u'\xa0', u' ') 


    title = final_soup.find("div", class_ = "heading").text
    titles.append(title)
    overviews.append(overview)
    
    #add to dict
    wisco_product_and_descriptions4[title] = overview
    

###Scrape Pharmaceutical & Vitamins
# check to make sure that the website link is good 
# current category is biologics
result = requests.get('https://www.warf.org/search-results/?searchwp=&search-technology=1&s_tech_category=pharmaceuticals-vitamin-d&date-range-start=&date-range-end=')

#puts all the html into src variable
src= result.content

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
base_url = ''

#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)

#After creating a means to get all the final urls create a final loop to make a request for every page and save the html
titles = []
overviews = []
wisco_product_and_descriptions5 = {}

for url in final_urls:
    res = requests.get(url)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')

    #key assumption: overview remains first section-content
    overview = final_soup.find_all("div", class_ = "section-content")[0].text
    overview = overview.replace(u'\n', u' ') 
    overview = overview.replace(u'\xa0', u' ') 

    title = final_soup.find("div", class_ = "heading").text
    titles.append(title)
    overviews.append(overview)
    
    #add to dict
    wisco_product_and_descriptions5[title] = overview
    

wisco_product_and_descriptions = {**wisco_product_and_descriptions1, **wisco_product_and_descriptions2, **wisco_product_and_descriptions3, **wisco_product_and_descriptions4, **wisco_product_and_descriptions5}



#convert dict to csv file
import csv

with open('wisconsin.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in wisco_product_and_descriptions.items():
            writer.writerow([key, value])
