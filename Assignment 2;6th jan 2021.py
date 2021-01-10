#!/usr/bin/env python
# coding: utf-8

# # Write a python program to remove duplicate from a list?

# In[1]:


def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [2,4,10,20,5,2,20,4]
print(remove(duplicate))


# # Write a python  program to get difference between two list?

# In[2]:


def Diff(li1,li2):
    return(list(list(set(li1)-set(li2))+list(set(li2)-set(li1))))
li1 = [10,15,20,25,30,35,40]
li2 = [25,40,35]
print(Diff(li1,li2))


# # Write a python program to get the frequency of elements in list?

# In[7]:


import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List: ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the list: ",ctr)


# # Write a python program to compute the similarity between two list?

# In[8]:


from collections import Counter
color1 = ["red","orange","green" ,"blue", "white"]
color2 = ["black","yellow","green","blue"]
counter1 = Counter(color1)
counter2 = Counter(color2)
print("Color1-Color2: ",list(counter1 - counter2))
print("Color2-Color1: ",list(counter2 - counter1))


# # write python program that takes a list and returns the longest one?

# In[10]:


def longestLength(a):
    max1 =len(a[0])
    temp = a[0]
    for i in a:
        if(len(i)>max1):
            max1= len(i)
            temp= i
    print("the word with the longestlength is: ",temp,"and length is ",max1)
a = ["one", "two", "three", "four"]
longestLength(a)


# # Write a python program to count the occurance  of each word  in a  sentence?

# In[27]:


def word_count(str):
    counts = dict()
    words =str.split()
    
    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word]  = 1
    return counts
print(word_count('the quick brown fox jumps over the lazy dog.'))


# # Write apython program  to count and display the vowels of a  given text? 

# In[38]:


def Check_Vow(string,vowels):
    final  = [each for each in string if each in vowels]
    print(len(final))
    print(final)
string  = "Welcome to python programming"
vowels  = "AaEeIiOoUu"
Check_Vow(string,vowels);


# # Write a python script to generate and print a dictionary that contains a number  (between 1and n) in the form (x,x*x)?

# In[39]:


n = int(input("Input a number "))
d = dict()

for x in range (1,n+1):
    d[x]=x*x
    
print(d)    


# # Write a  python program to combine two dictionary adding values for common keys?

# In[46]:


dict1 = {'a':100,'b':200,'c':300}
dict2 = {'a':300,'b':200,'d':400}
for key in dict2:
    if key in dict1:
        dict2[key]=dict2[key]+dict1[key]
    else:
        pass

print(dict2)


# # Write a python program to print all unique values in a dictionary?

# In[48]:


L = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"V":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
print("Original  List: ",L)
u_value = set(val for dic  in L for val in dic.values())
print("Unique Values: ",u_value)


# In[ ]:




