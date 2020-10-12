# This script pertains to the scraping of Purdue technologies
import requests
from bs4 import BeautifulSoup

# check to make sure that the website link piis good 
result = requests.get('https://inventions.prf.org/tech/10/innovations')
# print(result.status_code)

#puts all the html into src variable
src = result.content
# print(src)

#create beautiful soup object in order to add more functionality to content variable 
soup = BeautifulSoup(src,'lxml')

#python list to store all URL headers
atag = []
for td_tag in soup.find_all("td"):
    a_tag = td_tag.find('a', href=True)
    atag.append(a_tag)

#print(atag)
# gives all the urls in a python list with each element stored as strings 
urls = []
                   
for i in atag:
    if i is not None and i['href'][1:11] == 'innovation':
        urls.append(i['href'])       
#print(urls)
base_url = 'http://inventions.prf.org/'

#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)
#print(final_urls)
# ###################################################################################################
# #After creating a means to get all the final urls create a final loop to make a request for every page and save the html

description = []
for i in final_urls:
    res = requests.get(i)
    source = res.content
    final_soup = BeautifulSoup(src,'lxml')
    #print(final_soup)
    des = final_soup.find_all("td", {"style": "white-space: pre-line;"})
    description.append(des)

print(description)