import requests
import re
from bs4 import BeautifulSoup 

BASE_URL = "https://www.hotcity.co.nz/business-directory"

def scrapehotcity():

    response = requests.get(BASE_URL)

    soupforpages = BeautifulSoup(response.text, "html.parser")


    #Get list of business listings
    pages = soupforpages.findAll("a", {"title": re.compile("Go to page.*") })
    #print(pages)
    pagecnt = len(pages) + 1
    print("Number of pages - " + str(pagecnt))




    leadsList = []

    #loop through all the pages
    for i in range(pagecnt):
        print("Page: " + str(i))

        if(i == 0):
            response = requests.get(BASE_URL)
        else:
            response = requests.get(BASE_URL + "?page=" + str(i))
        
        soupforleads = BeautifulSoup(response.text, "html.parser")

        itemlist = soupforleads.findAll("div", {"class" : "directory__teaser"})
        print("Number of listings - " + str(len(itemlist)))

        for item in itemlist:
        


            try:
                name = item.find("div", {"property" : "dc:title"}).text
                address = item.find("div", {"class" : "adr"}).text
                phone = item.find("div", {"class" : "field-name-field-directory-phone-number"}).text

                leadsList.append([name,address,phone])
                print(name + " " + phone + " " + address.replace("\n", " "))
            except:
                pass
        
        
        
    return leadsList

scrapehotcity()