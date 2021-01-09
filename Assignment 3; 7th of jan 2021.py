#!/usr/bin/env python
# coding: utf-8

# # Write python function to find the max of three numbers?
# 

# In[8]:


def max(x,y):
    if x>y:
        return x
    return y
def maxx(x,y,z):
    return max(x,max(y,z))
print("max number is ",maxx(3,6,90))
    


# # write  a python function to check weather a passed string is paliandrome or not?
# 

# In[27]:


def isPalindrome(str):
    for i in range (0,int(len(str)/2)):
        if str [i] != str[len(str)-i-1]:
            return False
        return True
    s = "malayalam"
    ans = isPalindrome(s)
    if (ans):
            print("Yes")
    else:
        print("No")
        


# # write a python function that accepts a string and calculate  the numbers of uppercase and  lowercase lertters?

# In[28]:


def string_test(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for c in s:
        if  c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
        print("Original string : ",s)
        print("No. of Upper case characters: ",d["UPPER_CASE"])
        print("No. of Lower case characters: ",d["LOWER_CASE"])
        
string_test('The quick Brown Fox')        


# # Write a python function to sum all the numbers in a list?
# 

# In[40]:


total = 0
list1 = [11,5,17,18,23]
for ele in range (0,len(list1)):
    total = total + list1[ele]
    print("sum of all elements in given list: ",total)


# # write a python function to multiply all numbers in a list?

# In[41]:


def multiplylist(mylist):
    result =  1
    for x in mylist:
        result = result*x
    return result
list1 = [1,2,3]
list2 = [3,2,4]
print(multiplylist(list1))
print(multiplylist(list2))


# # write a python  funcion that takes a list and returns a new list with unique element?
# 

# In[46]:


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print (x),
list1=[10,20,10,30,40,40]
print("the unique  value form 1st list is")
unique(list1)
list2=[1,2,1,1,3,4,3,3,5]
print("/nthe unique values from 2nd list is")
unique(list2)
                


# In[ ]:




