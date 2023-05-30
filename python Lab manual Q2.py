#!/usr/bin/env python
# coding: utf-8

# In[7]:


file = open ("data.txt", "rt")
data = file.read()
words = data.split()
print ('Number of words in text file:', len(words))

