import requests
from bs4 import BeautifulSoup


# check to make sure that the website link is good 
# current category is biologics
result = requests.get('http://license.umn.edu/categories/1181_life-sciences/1195_biologics?query=')
# print(result.status_code)

#puts all the html into src variable
src= result.content
# print(src)

#create beautiful soup object in order to add more functionality to content variable 
soup = BeautifulSoup(src,'lxml')


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
# print(urls)
base_url = 'http://license.umn.edu/'

#create final list of links
final_urls = []
for i in urls: 
    final_string = "".join((base_url, i))
    final_urls.append(final_string)
# print(final_urls)

###################################################################################################
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

# TODO: create dict to map title of article ot description

# use dict comprehension to convert title and description lists to dict
minnesota_dict = {flattened_titles[i]: descriptions[i] for i in range(len(flattened_titles))}
print(minnesota_dict)