#!/usr/bin/env python
# coding: utf-8

# In[3]:


import smtplib
li = ["i798824@gmail.com"]
for dest  in li:
    s = smtplib.SMTP('smpt.gmail.com',587)
    s.starttls()
    s.login("sender_gmail_id","sender_email_id_password")
    message = "Message_you_need_to_send"
    s.sendmail("sender_gmail_id",dest,message)
    s.quit


# In[ ]:




