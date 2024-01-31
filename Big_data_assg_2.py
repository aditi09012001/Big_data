#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install requests')


# In[3]:


get_ipython().system('pip install pandas')


# In[4]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[43]:


product_name = []
product_price = []
product_rating = []
product_description=[]


# In[114]:


for i in range(2, 5):
    url = f"https://www.flipkart.com/search?q=mobiles+under+20000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_10_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_10_na_na_na&as-pos=3&as-type=RECENT&suggestionId=mobiles+under+20000&requestId=6ef26d5e-a966-4ea2-9a51-288012823d9f&as-searchtext=mobiles+under+20000&page={i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
    np_element = soup.find("a", class_="_1LKTO3")
    if np_element:
        np = np_element.get("href")
        cmp = "https://www.flipkart.com/" + np
    
    if box:
        names = box.find_all("div", class_="_4rR01T")
        for name in names:
            product_name.append(name.text.strip())
        
        prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
        for price in prices:
            product_price.append(price.text.strip())
        
        desc = box.find_all("ul", class_="_1xgFaf")
        for description in desc:
            product_description.append(description.text.strip())
        
        rating = box.find_all("div", class_="_3LWZlK")
        for rate in rating:
            product_rating.append(rate.text.strip())
    else:
        print(f"No products found on page {i}")



# In[115]:


dict={"Product Name": product_name,"Product Prices":
                product_price,"Product Ratings": product_rating,"Product Description":
                product_description}


# In[116]:


Data=pd.DataFrame.from_dict(dict, orient='index').T


# In[117]:


print("Product Name length:", len(product_name))
print("Product Price length:", len(product_price))
print("Product Rating length:", len(product_rating))
print("Product Description length:", len(product_description))


# In[118]:


Data[4582:4597]


# In[121]:


unique_product_names = Data['Product Name'].unique()
len(unique_product_names)


# In[129]:


import csv


# In[134]:


Data.to_csv("C:/Users/ASUS\Desktop/my books/mobile_phone_under_50000.csv")


# In[ ]:




