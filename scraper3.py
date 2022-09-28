from selenium import  webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    tablelt=soup.find("table", attrs={"class", "wikitable"})

    tblbdy=tablelt.find('tbody')
    tblrw=tblbdy.find_all('tr')

    for row in tblrw:
        col=row.find_all('td')
        print(col)
        temp=[]
        for col_data in col:
            data=col_data.text.strip()
            temp.append(data)
        planets_data.append(temp)

scrape()

sters=[]
for i in range(0,len(planets_data)):
    stnm=planets_data[i][1]
    dis=planets_data[i][3]
    mas=planets_data[i][5]
    rad=planets_data[i][6]
    lim=planets_data[i][7]
    reqs=[stnm,dis,mas,rad,lim]
    sters.append(reqs)


# Define Header
headers = ["stnm", "dis", "mas", "rad", "lim"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(sters, columns=headers)

# Convert to CSV
planet_df_1.to_csv('scraped_data_bs.csv',index=True, index_label="id")