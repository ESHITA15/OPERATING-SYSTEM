#!/usr/bin/env python
# coding: utf-8

# In[11]:


firstfile= open('test.txt','r')  
secondfile= open('Dictionary.txt','a')
for line in firstfile:    
    secondfile.write(line)    
file = open("data.txt", "rt")
data = file.read()
words = data.split()
print('Number of words in text file :', len(words))
file = open("data.txt", "rt")
data = file.read()
words = data.split()
print('Number of words in text file :', len(words))


# In[ ]:




