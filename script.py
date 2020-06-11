#!/usr/bin/env python
# coding: utf-8

# In[73]:


import requests
from bs4 import BeautifulSoup
import pandas 

l = []
base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
pg_nr = soup.find_all("a" , {"class" : "Page"})[-1].text
for page in range(0,int(pg_nr)*10,10):
    header_str = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    r = requests.get(base_url + str(page) + ".html" , headers = header_str)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    a = soup.find_all("div",{"class":"propertyRow"})
    for item in a:
        d = {}
        d["Price"] = item.find("h4",{"class","propPrice"}).text.strip()
        d["Address"] = item.find_all("span",{"class","propAddressCollapse"})[0].text
        try:
            d["Locality"] = item.find_all("span",{"class","propAddressCollapse"})[1].text
        except:
            d["Locality"] = "None"
        try:
            d["Beds"] = item.find("span",{"class","infoBed"}).find("b").text.strip()
        except:
            d["Beds"] = "None"
        try:
            d["SqFt."] = item.find("span",{"class","infoSqFt"}).find("b").text.strip()
        except:
            d["SqFt."] = "None"
        try:
            d["Full Bath"] = item.find("span",{"class","infoValueFullBath"}).find("b").text.strip()
        except:
            d["Full Bath"] = "None"
        try:
            d["Half Bath"] = item.find("span",{"class","infoValueHalfBath"}).find("b").text.strip()
        except:
            d["Half Bath"] = "None"
        for column in item.find_all("div",{"class":"columnGroup"}):
            for feature_group,feature_name in zip(column.find_all("span",{"class":"featureGroup"}) ,column.find_all("span",{"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        l.append(d)
        
df = pandas.DataFrame(l)
df.to_csv("Outputf.csv")


# In[ ]:




