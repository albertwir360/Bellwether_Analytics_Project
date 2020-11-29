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
    base_url = 'http://msut.technologypublisher.com/'

    #create final list of links
    final_urls = []
    for i in urls: 
        final_string = "".join((base_url, i))
        final_urls.append(final_string)



    #After creating a means to get all the final urls create a final loop to make a request for every page and save the html
    descriptions = []
    titles = []


    for i in final_urls:
        res = requests.get(i)
        source = res.content
        soup = BeautifulSoup(source,'lxml')

        title = soup.find('h2', class_='large-title').text

        text = ""
        # account for different text styles
        for span in soup.find_all("span", style="font-family: 'Arial';font-style: Normal;font-size: 13.33px;"):
            text += span.text
        for span in soup.find_all("span", style="font-family: 'Arial';font-size: 13.33px;"):
            text += span.text
        for span in soup.find_all("span", style="font-family: 'Arial';font-style: Normal;font-size: 13.3333333333333px;"):
            text += span.text

        for span in soup.find_all("span", style="font-size:14px"):
            text += span.text

        if (text != ""):
            descriptions.append(text)
            titles.append(title)

    # remove other unwanted characters
    descriptions = [remove_special_char(text) for text in descriptions]

    # create dict to map title of article to description
    # use dict comprehension to convert title and description lists to dict
    tech_dict = {titles[i]: descriptions[i] for i in range(len(titles))}
    return tech_dict


# URL Codes for each technology category:

# http://msut.technologypublisher.com/searchresults.aspx?q=Biotechnology&type=c
# http://msut.technologypublisher.com/searchresults.aspx?q=Medical&type=c
# http://msut.technologypublisher.com/searchresults.aspx?q=Pharmaceutical&type=c

# store dictionaries for each technology 
biotech_dict = scrape_technology('http://msut.technologypublisher.com/searchresults.aspx?q=Biotechnology&type=c')
print("biotech done")
med_dict = scrape_technology('http://msut.technologypublisher.com/searchresults.aspx?q=Medical&type=c')
print("medical done")
pharma_dict = scrape_technology('http://msut.technologypublisher.com/searchresults.aspx?q=Pharmaceutical&type=c')
print("pharmaceutical done")




# create dict of all dicts
msu_dict = {**biotech_dict, **med_dict, **pharma_dict}


with open('msu.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in msu_dict.items():
            writer.writerow([key, value])



