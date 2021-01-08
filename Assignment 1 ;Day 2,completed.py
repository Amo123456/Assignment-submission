#!/usr/bin/env python
# coding: utf-8

# # (2x+5/x^2+5x+6)

# In[12]:


x = float(input("enter the value of x"))
x = int(input("enter the integer value"))
y = (2*x+5)/(x^2+5*x+6)
print("the result is: ",y)


# # (x^2+5x+6/2x+5)
# 

# In[14]:


x = float(input("enter the coefficent number"))
x = int(input("enter the integer value"))
y = (x^2+5*x+6)/(2*x+5)
print("the result is: ",y)


# # (2x-3)(x+9)
# 

# In[16]:


x  = 5
y = (2*x-3)*(x+9)
print("the result is: ",y)


# Create a username and password login file using nestedwhile loop?

# In[26]:


print('Enter correct username and password')
count=0
if count==4:
    print('account has block')
while count < 5:
    username = input('enter username: ')
    password = input('enter password: ')
    if password== 'IND' and username=='INDIA':
        print('congratulation LOGIN succesfully')
        break
    else:
        print('incorrect password. Try again.')
        count +=1
        if count==5:
            print('Account has temporary block')


# In[ ]:




