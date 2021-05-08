#!/usr/bin/env python
# coding: utf-8

# In[74]:


## 3. Sorunun Cevabı Aşağıdadır

a = "Ah5me4t"
b = "M9eHm4eT"
c = "Ha3K5a1n"

list1 = [a,b,c]
sonuc = ""
x = 0

for i1 in list1:
    rev = list1[x]
    for i2 in rev:
        if i2.isdigit():
            rev = rev.replace(i2 , '')

    list1[x] = rev
    x = x + 1

for y in list1:
    sonuc = sonuc + '-' + y
    
print(sonuc[1:])


# In[ ]:




