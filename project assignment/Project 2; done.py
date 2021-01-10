#!/usr/bin/env python
# coding: utf-8

# In[25]:


import random
name = input("what is the movie name?")
print("Good Luck!|",name)
words = ['rainbow','computer','gaura','science','mathematics','pogramming','reverse','water','board','geeks','condition','programming']
word = random.choice(words)
print("Guess the characters")
guesses = ""
turns = 5
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You win")
        print("the word is : ", word)
        break
    guess = input("guess  a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("wrong")
        print("You have",+turns,'more guesses')
        if turns == 0:
            print("You Loose")
    



# In[ ]:


""

