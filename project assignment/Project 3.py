#!/usr/bin/env python
# coding: utf-8

# # Create  a instagram downloader by using command prompt?

# In[10]:


import requests 
from bs4 import BeautifulSoup as bs 
import json
import random
import os.path
insta_url = 'https://www.instagram.com'
insta_username = input('enter username of instagram: ')
response = requests.get(f"{insta_url}/{insta_username}/")
if response.ok:
    html = response.text
    bs_html = bs(html,features = "lxml")
    bs_html = bs_html.text
    index = bs_html.find('profile_pic_url_hd')+21
    remaning_text = bs_html[index:]
    remaning_text_index = remaning_text.find('requested_by_viewer')-3
    string_url = remaning_text[:remaning_text_index].replace("\\u0026","&")
    print(string_url,"\n \n downloading..........")
    while True:
        filename = 'pic'+str(random.randint(1,100000))+'.jpg'
        file_exist= os.path.isfile(filename)
        if not file_exist:
            with open(filename,'wb+')as handle:
                if not response.ok:
                    print(response)
                for block in response.iter_content(1024):
                             if not block:
                                 break
                             handle.write(block)
        else:
                          continue
                          break
                          print("\n               downloading completed............")


# In[ ]:




