import requests
from bs4 import BeautifulSoup
import re
import csv
import numpy as np 

TAG_RE = re.compile(r'<[^>]+>')
CHAR_RE = re.compile(r'[^.\'A-Za-z0-9]+')


def remove_tags(text):
    return TAG_RE.sub("", text)

def remove_special_char(text):
    return CHAR_RE.sub(" ", text)


def scrape_technology(url):
    result = requests.get(url)

    # puts all the html into src variable
    src= result.content

    # create beautiful soup object in order to add more functionality to content variable 
    soup = BeautifulSoup(src,'lxml')

    # python list to store all URL headers
    atag = []
    for h2_tag in soup.find_all("h2"):
        a_tag = h2_tag.find('a', href=True)
        atag.append(a_tag)

    # gives all the urls in a python list with each element stored as strings 
    urls = []
    for i in atag:
        if i is not None:
            urls.append(i['href'])       
    base_url = 'http://license.umn.edu/'

    # create final list of links
    final_urls = []
    for i in urls: 
        final_string = "".join((base_url, i))
        final_urls.append(final_string)

    # After creating a means to get all the final urls create a final loop to make a request for every page and save the html
    descriptions = []
    titles = []

    for i in final_urls:
        res = requests.get(i)
        source = res.content
        final_soup = BeautifulSoup(source,'lxml')
        for tag in final_soup.find_all('div', class_='technology'):
            text = tag.find_all('p')
            title = tag.find_all('h1')
            titles.append(title)
            descriptions.append(text)

    # clean titles
    # remove the empty lists
    titles = titles = titles[0::2]
    # flatten list of lists into list and convert to string
    flattened_titles = [str(title) for subtitle in titles for title in subtitle]
    # remove the h1 tags
    flattened_titles = [title.strip("</h1>") for title in flattened_titles]

    # remove empty elements
    descriptions = [elem for elem in descriptions if elem]

    # clean descriptions
    # we don't want the first two elements in each list in descriptions list as they do not contain description info
    descriptions = [description[2:] for description in descriptions]

    # remove the empty lists and convert EACH ELEMENT TO STRING
    descriptions = [str(description) for description in descriptions if description != []]

    # remove html tags
    descriptions = [remove_tags(text) for text in descriptions]
    # remove other unwanted charaacters
    descriptions = [remove_special_char(text) for text in descriptions]


    # create dict to map title of article to description

    # use dict comprehension to convert title and description lists to dict
    tech_dict = {flattened_titles[i]: descriptions[i] for i in range(len(flattened_titles))}

    return tech_dict


# URL Codes for each technology category:

# biologics - 1195_biologics
# biomarkers - 1198_biomarkers
# cellular therapeutics - 1196_cellular-therapeutics
# diagnostic imaging - 1211_diagnostics-imaging
# human health - 4451_human-health
# medical devices - 1214_medical-devices
# nueroscience - 5252_neuroscience
# pharma - 1197_pharmaceuticals


# store dictionaries for each technology 
biologics_dict = scrape_technology('http://license.umn.edu/categories/1181_life-sciences/1195_biologics?query=')
print("biologics done")
biomarkers_dict = scrape_technology('http://license.umn.edu/categories/1181_life-sciences/1198_biomarkers?query=')
print("biomarkers done")
cellular_dict = scrape_technology('http://license.umn.edu/categories/1181_life-sciences/1196_cellular-therapeutics?query=')
print("cellular therapeutics done")
diagnostics_dict = scrape_technology('http://license.umn.edu/categories/1181_life-sciences/1211_diagnostics-imaging?query=')
print("diagnostic/imaging done")
human_dict = scrape_technology('http://license.umn.edu/categories/1181_life-sciences/4451_human-health?query=')
print("human health done")
medical_dict = scrape_technology('http://license.umn.edu/categories/1181_life-sciences/1214_medical-devices?query=')
print("medical devices done")
neuro_dict = scrape_technology('http://license.umn.edu/categories/1181_life-sciences/5252_neuroscience?query=')
print("neuroscience done")
pharma_dict = scrape_technology('http://license.umn.edu/categories/1181_life-sciences/1197_pharmaceuticals?query=')
print("pharmaceuticals done")




# create dict of all dicts
minnesota_dict = {**biologics_dict, **biomarkers_dict, **cellular_dict, **diagnostics_dict, **human_dict, **medical_dict, **neuro_dict, **pharma_dict}


with open('minnesota.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in minnesota_dict.items():
            writer.writerow([key, value])



