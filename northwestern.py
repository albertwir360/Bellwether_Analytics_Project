# This script pertains to the scraping of Northwestern technologies
import requests
from bs4 import BeautifulSoup
import re
#import psycopg2


# def listToString(s):  
    
#     # initialize an empty string 
#     str1 = " " 
    
#     # return string   
#     return (str1.join(s)) 
        
        
     

# # Database Connection Variables
# DB_NAME = "Big_10"
# DB_USER = "Bellwether123@transfer-tech"
# DB_PASS = "Consulting123"
# DB_HOST = "transfer-tech.postgres.database.azure.com"
# DB_PORT = "5432"

# connection = psycopg2.connect(
#             host = DB_HOST,
#             dbname = DB_NAME,
#             user = DB_USER,
#             password = DB_PASS,
#             port = DB_PORT,   
#         )
# print("connection established")


# cursor = connection.cursor()
# # Drop previous table of same name if one exists
# cursor.execute("DROP TABLE IF EXISTS technology;")
# print("Finished dropping table (if existed)")

# # Create a table
# cursor.execute("CREATE TABLE technology (id serial PRIMARY KEY, technology_name VARCHAR(100), author TEXT, description TEXT);")
# print("Finished creating table")

# # Insert some data into the table




#function to webscrape northwestern webpages... this will be looped through 
def northwestern(): 
    #request the website for html
    result = requests.get('https://www.invo.northwestern.edu/technologies/technologies/industry-pipelines/therapeutics/index.html')
    #store the html into a variable
    src= result.content
    #create beautiful soup object which give added functionality for parsing and store this into "soup" variable
    soup = BeautifulSoup(src,'lxml')
    #create and store atags in list
    h5 = []
    for h5_tag in soup.find_all("h5"):
        h5.append(h5_tag.get_text()) # title of the technology
    
    # want to access number of boxes in each stage
    #id, dialog...Desc (different numbers (e.g. 1-1, 1-2, 1-6))
    # each box tag corresponds to stageNumber-technologyNumber
    # 6th box in stage 1 is 1-6, 7th box in stage 2 is 2-7
    # below gets each box's id 
    id = []
    for tag in soup.find_all("a", {"class" : "open-modal"}):
        id.append(tag.get('id'))
    # creating dialog1-1Desc tags but replace the "1-1" accordingly for each box
    # creating full id tags
    
    full_id = []
    for i in range(len(id)):
        full = "dialog" + id[i] + "Desc"
        full_id.append(full)
    
    #for div in soup.find_all("div", {"id" : "dialog1-6Desc"}):
        #print(div.get_text()) 
    #below is the generalized version of the above^
    info = [] # this lists short description, primary inventor and tags
    atag = []
    description_urls = [] # this gives a list of all the urls that lead to the full description
    for f in range(len(full_id)):
        for div in soup.find_all("div", {"id" : full_id[f]}):
            info.append(div.get_text()) 
            a_tag = div.find('a', href=True)
            
            atag.append(a_tag)
            for i in range(len(atag)):
                if atag[i] is not None:
                    description_urls.append(atag[i]['href']) 
    
    # remove \xa0 tag 
    info = [i.strip("\xa0") for i in info]
    
    #remove empty 
    info = [i for i in info if i != ""]
    
    
    #BELOW ARE COMMENTS RELATED TO MSU TEMPLATE MYSQL DATABASE - didn't remove bc it might be useful 
    # cursor.execute("INSERT INTO technology (technology_name, author,description) VALUES (%s, %s, %s);", (z, y, x))



    # for i in range(len(x)):
    #     cursor.execute("INSERT INTO technology (technology_name, author,description) VALUES (%s, %s, %s);", (str(z[i]), str(y[i]), str(x[i])))
    #     print("Inserted a row of data")
 

northwestern()