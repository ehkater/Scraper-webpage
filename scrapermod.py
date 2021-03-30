import requests
import re
from bs4 import BeautifulSoup 


BASE_URL = "https://www.nzdirectory.co.nz/business-services.html"



def nzdirectory():

    response = requests.get(BASE_URL)

    soupforpages = BeautifulSoup(response.text, "html.parser")


    
    pages = soupforpages.findAll("a", {"title": re.compile("page.*") })
   
    pagecnt = len(pages) + 1
    print("Number of pages - " + str(pagecnt))




    leadsList = []

    
    for i in range(pagecnt):
        print("Page: " + str(i))

        if(i == 0):
            response = requests.get(BASE_URL)
        else:
            response = requests.get(BASE_URL + "?page=" + str(i))
        
        soupforleads = BeautifulSoup(response.text, "html.parser")

        itemlist = soupforleads.findAll("li", {"class" : "premium"})
        print("Number of listings - " + str(len(itemlist)))

        for item in itemlist:
        


            try:
                name = item.find("a", {"class" : "premium_text"}).text
                address = item.find("p", {"class" : "address"}).text
                phone = item.find("p", {"class" : "address"}).text
                splice = phone.find("+")

                leadsList.append([name,address,phone])
                print(name + " " + phone + " " + address.replace("\n", " "))
                print(splice)
                
            except:
                pass
        
        
        
    return leadsList

nzdirectory()

