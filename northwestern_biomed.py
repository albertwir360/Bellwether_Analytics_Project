import requests
from bs4 import BeautifulSoup

#request the website for html
result = requests.get('https://www.invo.northwestern.edu/technologies/technologies/industry-pipelines/biomarkers-biomedical-research-tools.html')
    #store the html into a variable
src= result.content
    #create beautiful soup object which give added functionality for parsing and store this into "soup" variable
soup = BeautifulSoup(src,'lxml')

for tr in soup.find_all("tr", {"class" : "stripe"}):
    a_tag = tr.find_all("a", href=True)
    print(tr)
