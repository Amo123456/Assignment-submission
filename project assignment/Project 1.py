#!/usr/bin/env python
# coding: utf-8

# # Develop a cryptography app using python?

# In[9]:


from cryptography.fernet import Fernet
def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("Secret.key","wb")as key_file:
        key_file.write(key)
def load_key():
    """
    Load the previously generated key
    """
    return open("Secret.key","rb").read()
def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_mmessage)
    print(encrypted_mmessage)
if __name__  == "__main__":
    encrypt_message("encrypt this message")


# In[ ]:




