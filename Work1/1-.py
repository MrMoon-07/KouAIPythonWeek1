#!/usr/bin/env python
# coding: utf-8

# In[86]:


a = input("Değer giriniz: ")

if a.isnumeric():
    a = int(a)
else:
    print("Hatalı girdi, tekrar deneyiniz.")
    
if a%2 == 0:
    print("Girilen değer çifttir")
else:
    print("Girilen değer tektir")

