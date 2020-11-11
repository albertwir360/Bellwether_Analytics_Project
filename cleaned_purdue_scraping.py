# This script pertains to the scraping of Purdue technologies
import requests
from bs4 import BeautifulSoup
import csv

result = requests.get('https://inventions.prf.org/tech/10/innovations')
# link above is for biomedical technologies, but this script can parse and clean all below links
# providing links for all tech here:
    # biotech: https://inventions.prf.org/tech/1/innovations csv made
    # medical: https://inventions.prf.org/tech/19/innovations csv made
    # pharma: https://inventions.prf.org/tech/21/innovations csv made
    # biomed: https://inventions.prf.org/tech/10/innovations

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
base_url = 'http://inventions.prf.org'

#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)

# ###################################################################################################
# #After creating a means to get all the final urls create a final loop to make a request for every page and save the html

description = []
tech_name = []
author = []
for i in final_urls:
    res = requests.get(i)
    source = res.content
    final_soup = BeautifulSoup(source,'lxml')
    name = final_soup.find("h1").get_text() # located names of technologies
    tech_name.append(name)
    # finding all descriptions which were within td tags
    for td_tag in final_soup.find_all("td", {"style" : "white-space: pre-line;"}):
        description.append(td_tag.get_text())
    for ul in final_soup.find_all("ul", {"style" : "list-style: none; padding: 0;"}): # finding names of authors
        categories = ul.select("li a")
        for i in categories:
            if i['href'][1:7] == 'person': # need to do this b/c there were multiple matches for the ul tag
                author.append(i.get_text())
            
# creating dict

purdue_dict = {tech_name[i]: description[i] for i in range(len(tech_name))}
with open('purdue_biomed.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in purdue_dict.items():
            writer.writerow([key, value])

with open('purdue_biomed.csv') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)
#print(purdue_dict)





